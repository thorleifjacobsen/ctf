import requests

url = "http://motherload.td.org.uit.no:8012"

response = requests.get(f"{url}?digit=2")
while "STARTING, HURRY!" not in response.text:
    response = requests.get(url)

for digit in [4, 6, 8, 10]:
    res = requests.get(f"{url}?digit={digit}")
    print(f"Response for digit {digit}: {res.text.strip()}")
