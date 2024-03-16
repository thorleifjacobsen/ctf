using System.Data;
using System.Runtime.Versioning;
using System.Security.Cryptography;
using Dapper;
using Microsoft.Data.Sqlite;
using ZXing.SkiaSharp;

[assembly: SupportedOSPlatform("Linux")]

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddScoped<IDbConnection>((sp) => new SqliteConnection($"Data Source=data.sqlite"));

var app = builder.Build();
var flag = Environment.GetEnvironmentVariable("flag") ?? "1753c{fake_flag}";

using (var db = app.Services.GetService<IDbConnection>())
{
    await db.ExecuteAsync("CREATE TABLE Tickets (id INTEGER PRIMARY KEY, code VARCHAR(36), hash VARCHAR(40))");
    await db.ExecuteAsync($"INSERT INTO Tickets (id, code, hash) VALUES (1, '{flag}', 'admin-needs-no-hash')");
}

(string Code, string Hash) ParsePDF(Stream pdfStream)
{
    using var memoryStream = new MemoryStream();
    pdfStream.CopyTo(memoryStream);

    var bitmap = PDFtoImage.Conversion.ToImage(memoryStream, leaveOpen: true);

    var reader = new BarcodeReader();
    var result = reader.Decode(bitmap);

    using var sha1 = SHA1.Create();

    memoryStream.Position = 0;
    byte[] hashBytes = sha1.ComputeHash(memoryStream);
    var hash = BitConverter.ToString(hashBytes).Replace("-", "").ToLowerInvariant();

    return (result.Text, hash);
}

app.MapPost("upload", async (HttpContext context, IDbConnection db) =>
{
    try
    {
        var inputStream = context.Request.Form.Files[0].OpenReadStream();
        var (code, hash) = ParsePDF(inputStream);

        if (!Guid.TryParse(code, out var result))
            Results.BadRequest("Ticket must have a GUID in QR code");

        await db.QueryAsync($"INSERT INTO Tickets (code, hash) VALUES ('{code}', '{hash}')");

        return Results.Ok("Ticket added");
    }
    catch (Exception)
    {
        return Results.UnprocessableEntity("Request must contain valid PDF with QR code containg UUID");
    }
});

app.MapPost("verify", async (HttpContext context, IDbConnection db) =>
{
    try
    {
        var inputStream = context.Request.Form.Files[0].OpenReadStream();
        var (code, hash) = ParsePDF(inputStream);

        var existingHash = await db.QueryFirstOrDefaultAsync<string>($"SELECT * FROM Tickets WHERE hash like '{hash}'");

        if (existingHash is null)
            return Results.NotFound("Ticket forged!");

        var ticket = await db.QueryFirstOrDefaultAsync($"SELECT * FROM Tickets WHERE code like '{code}'");

        return Results.Ok(ticket);
    }
    catch (Exception)
    {
        return Results.UnprocessableEntity("Request must contain valid PDF with QR code containg UUID");
    }
});



app.Run();

