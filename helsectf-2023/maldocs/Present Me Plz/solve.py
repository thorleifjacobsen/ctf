with open('./DSC002.jpeg', 'rb') as f:
    data = f.read()

data = data[2:] 
x = 24
decodedData = []
for i in data:
    x = (29 * x + 49) % 256
    decodedData.append((i ^ x))

with open("flag.png", "wb") as f:
    f.write(bytes(decodedData))