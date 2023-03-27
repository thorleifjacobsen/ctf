# alle_gode_ting_er_tre (500)

Enkel enkoding, eller ikke, vi satser på at alle gode ting er tre når vi roter alt sammen og bruker enkel kryptering!

[source.py](source.py) [output.txt](output.txt)

# Writeup

Quick reverse shows me that this script does the following:

1. Loads the flag and verifies that it is modulus of 3.
2. Splits the flag into pieces of 3. So `hel` `sec` `tf{`
3. Creates keys by using a scramble function of each part of the splitted flag.
4. Moves the last part of the key to front position. 
5. Loops through the pices of the flag and xor's them with the key in the same location. 
6. Put them into a ciphertext variable. 

The key thing here is that they move the last part of the key to the front. So if the key was like this:

```python
[scramble(b'hel'), scramble(b'sec'), scramble(b'tf{')]
```

the first key would now be the scramble of `tf{` like this:

```python
[scramble(b'tf{'), scramble(b'hel'), scramble(b'sec')]
```

Based on this we can now certainly say that we know from the second part of the flag and onwards the `key` they use. And with XOR as long as we know 2 we can get the last one. We know the ct value as we can extract that from the `ciphertext` in `output.txt`. We know the `key`. We to not know the `pt`

```python
ct = to21bit(pt)^key
```

So I wrote this simple script to decode the flag:


```python
# This is the CT we're given
ct = 91288880675628035011093545005790682206962326526026631772248877471574034941238763064368507363758616986

# Skip the first we do not know what this key is.
# As the key is based on the last 3 bytes of the flag which we do not have yet.
ct >>= 21

# We know the key for the next 3 bytes are `hel` as the flag starts with that.
keyPlaintext = b"hel"

# We build our flag starting with the 3 known one.
flag = keyPlaintext.decode()

while ct > 0:

    # Extract 21 bits 
    tre = ct & 0b111111111111111111111 # 21 bits
    # Remove the 21 bits we extracted from the CT
    ct >>= 21

    # So we use scrambled keyPlaintext XOR'ed with the 21 bits we extracted to get the value
    key = tre^scramble(keyPlaintext)

    # I split the 12 bits into 3 bytes and convert them to ascii
    keyPlaintext = chr(key >> 14 & 127) + chr(key >> 7 & 127) + chr(key & 127)
    
    # Add those to the flag
    flag += keyPlaintext

    # I convert the 3 characters to bytes just to make our life simpler. 
    keyPlaintext = keyPlaintext.encode()

    # Then we can restart the loop

# Lastly print the whole flag
print(flag)
```

See [solution.py](solution.py) for the whole script. We borrow the `scramble` function from [source.py](source.py)

# Flag

```
helsectf{Fowler-Noll-Vo_hAsH_fUnkSj0n_3r_raSk!!}
```