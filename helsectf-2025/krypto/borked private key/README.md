# borked private key

Fila borked_private_key.pem har blitt kopiert over en støyete forbindelse og en protokoll uten feilkorrigering. Derfor har det blitt noen bitfeil. Heldigvis bare tre i hele fila. Vi vet at én bit er feil i hver av modulus(n) og prime1(p) og prime2(q).

OpenSSL er så snill at den ikke nekter å lese ut verdiene i fila selv om nøkkelen er ødelagt: `openssl rsa -inform der -in borked_private_key.der -noout -text`

Hadde nøkkelen vært uten linjestøy kunne du dekryptert fila `flagg.txt.encrypted` med kommandoen `openssl pkeyutl -decrypt -inkey nonborked_private_key.der -in flag.txt.encrypted`

Klarer du det likevel?

[⬇️ borked_private_key.zip](./borked_private_key.zip)

# Writeup

Using `openssl rsa -inform der -in borked_private_key.der -noout -text` to export `n` (modulus), `p` (prime1) and `q` (prime2) from the provided `borked_private_key.der` file we can brute recreate them. As they say there is only one bit error in each of the modulus, prime1 and prime2.

RSA can be caculated with the following formula:

```
n = p * q
```

Using this we can coonvert the hex values to numbers and create a triple loop to first try all combinations. When we find a combination where `n == p * q` with only flipping one bit of each we have found the correct values.

```python
n_hex = "00a747f22eb..."
p_hex = "00bb9c2fb22..."
q_hex = "00e442a5343..."

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
```



I goot the correct numbers now and too create a new der file i used this script:


```python
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes

n_fixed = "00a747f22eb..."
p_fixed = "00bb9c2fb22..."
q_fixed = "00e442a5343..." 
n = bytes.fromhex(n_fixed)
p = bytes.fromhex(p_fixed)
q = bytes.fromhex(q_fixed)

N = bytes_to_long(n)
P = bytes_to_long(p)
Q = bytes_to_long(q)

e = 65537

# Compute phi(n) = (p-1)*(q-1).
phi_n = (P - 1) * (Q - 1)

# Compute d = e^{-1} mod phi(n).
# Python 3.8+ has pow() with a 3-argument form that does modular inverse:
d = pow(e, -1, phi_n)

key = RSA.construct((N, e, d, P, Q))

# Now you can export it in DER or PEM form:
with open("nonborked_private_key.der", "wb") as f:
    f.write(key.export_key(format="DER"))

```




openssl pkeyutl -decrypt -inkey nonborked_private_key.der -in flag.txt.encrypted

Now lets make them to bytes for math:

```pyhon
n = bytes.fromhex(n)

# Flag

```

```