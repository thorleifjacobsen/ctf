import pyshark

cap = pyshark.FileCapture("fangede_pakker.pcap")
all_ips = {}
all_ttl = {}

for packet in cap:
    binary_string = bytes.fromhex(packet.data.data).decode('utf-8')
    ascii_char = chr(int(binary_string, 2))
    
    if packet.ip.dst in all_ips:
        all_ips[packet.ip.dst] += ascii_char
        all_ttl[packet.ip.dst] += int(packet.ip.ttl)
    else:
        all_ips[packet.ip.dst] = ascii_char
        all_ttl[packet.ip.dst] = int(packet.ip.ttl)

    # if packet.ip.dst == "127.88.199.49": 
    #     print(packet.ip.ttl,all_ttl[packet.ip.dst])

for k, v in all_ips.items():
    print(f"{k} = {v} = {all_ttl[k]}")
