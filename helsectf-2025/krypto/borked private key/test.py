n_hex = "00a747f22ebd523ab3a3420b395fed6082debcf05cfcae23c54dc270f90d7c56d00cbfed5651abb9d041aca43fd386dc24518fd51db96544af29bd819d7290ad00e2fe01434b1423d113e6a8228ad82965fb8d04f1288447a9d97f8bfe2aa04931cda5beafd0886bfde16523584543af6833b8aa810cd49d0d74e45a423b87e61f349b35e560261b2d458fc674447676e880b72a62ef675296dd941972d3a0927336cd47034da02ea2de03960376927699efb18aa7f672a9ade2f2d8461b576bc3c6be3d21dbb3f860e8bf1983d01e9b192d8a4dcb8367dd124c84fff66ba62f177d22c908fc4b2be0dc3212c8db95b0e23d54c23e880d2454f45c011338609067"
p_hex = "00bb9c2fb22dc5b5f16518fbe19408fba15e9bbc6eb699c88e87bf81fa152888d653a43cb3b3f77d037045cbeaaba4444d026016f4000c6db312844638756cf4181954336a3e8ab252e7f135a8d8d39dd5490574540ffb1cf4a411e06d6cd717fa6679f8790d001580af97473a48998bd5b514015f39787c34f7b3358dab5526db"
q_hex = "00e442a5343c1e82347b01c59050d2e29987e8fa8347969efde9eb9d9b215ce9ae1c9bc6d377d9d887bded0d0944ae58190ea75d52413868aba64bcc39912c3727a46f64d9e37d08423d7eb67ebaff103a062017ddab02339a16f4955d8358620fd737a77e0e25bbab047a6417d720796ebe1e7345b892d3661947dddb0d977465"

n  = bytes.fromhex(n_hex)
p  = bytes.fromhex(p_hex)
q  = bytes.fromhex(q_hex)

def swap_one_byte(data):
    barray = bytearray(data)
    for i in range(len(barray)):
        for byte in range(255):
            barray[i] = byte    # Change the byte to 0-255
            yield bytes(barray)
            barray[i] = data[i] # Reset the byte to original value


for new_n in swap_one_byte(n):
    for new_p in swap_one_byte(p):
        for new_q in swap_one_byte(q):
        
            n_int = int.from_bytes(new_n, "big")
            p_int = int.from_bytes(new_p, "big")
            q_int = int.from_bytes(new_q, "big")
            
            if n_int == p_int * q_int:
                print(f"n: {n_int}")
                print(f"p: {p_int}")
                print(f"q: {q_int}")
                break