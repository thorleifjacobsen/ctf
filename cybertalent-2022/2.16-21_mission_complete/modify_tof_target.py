import struct

with open("missile.1.3.37.fw", "rb") as f:
  data = f.read().hex()


start = 0x00019010 * 2
length = 24 * 2
target = data[start:start+length]
target = bytes.fromhex(target)
format_string = "<" + "d"*(len(target)//8)
values = struct.unpack(format_string, target)
values = list(values)

# Set new target here
values[0] = 4224766.330344398
values[1] = -3991030.5468107667
values[2] = 2610108.3556840476

values = tuple(values)

newtarget = struct.pack(format_string, *values)

print(f"Old data: {data[start:start+length]}")
data = data.replace(target.hex(), newtarget.hex())
print(f"New data: {data[start:start+length]}")

# Set TOF value here.
tof = 5 

data = data.replace("00e09040", struct.pack("<d", tof).hex()[-8:])
data = bytes.fromhex(data)

with open(f"missile_mod.fw", 'wb') as f:
    f.write(data)
