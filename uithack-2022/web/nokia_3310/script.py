import requests, time

url = "http://motherload.td.org.uit.no:8001"

response = requests.get(f"{url}/message/new")
data = response.json()

print(f"Got message id: {data['message_id']}")
headers = { "Content-Type": "application/json" }

for digit in [8,8,8,4,4,4,4,8,8,4,4,4,2,2]:
    response = requests.post(f"{url}/button/{digit}", json=data, headers=headers)
    print(f"{digit} = {response.status_code}")

# Sleep due to more characters at same button
time.sleep(0.5)

# Somehow I needed to add a random number and a blank comma at the end for it to register the g...
for digit in [2,2,2,2,5,5,5,2,3,0,0,3,3,3,3,5,5,5,5,2,2,4,4,0,]: 
    response = requests.post(f"{url}/button/{digit}", json=data, headers=headers)
    print(f"{digit} = {response.status_code}")


res = requests.post(f"{url}/message/{data['message_id']}/send", headers=headers)
print(res.text)
