# Added 0000 padding to counter out of bounds.
ct = bytearray(bytes.fromhex("0000" + "6671" + "75516852" + "6e746b685269736d" + "6e686c466e4e5264" + "584d5241515a4448"))[::-1]

testFlag = "helsectf{" # I know this part, save some time.

for l in range(0,100):
  for nextByte in range(32,127):
    prevByte = ord(testFlag[-1]) # Last letter
   
    if (prevByte ^ nextByte) + 0x3b == int(ct[len(testFlag)-1]):
      testFlag += chr(nextByte)
      print(testFlag)
