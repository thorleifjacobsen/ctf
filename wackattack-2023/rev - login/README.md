# Login (beginner)

Please log in before starting the rev category

Author: krloer

📎 [login](login)

# Writeup

Running `strings` is often the first test on unknown binaries and this shows:

```bash
└─$ strings -n 10 login 
/lib64/ld-linux-x86-64.so.2
__libc_start_main
__cxa_finalize
GLIBC_2.2.5
GLIBC_2.34
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
Malloc failed. Contact a ctf admin.
Hi there! Please log in.
Username: 
Password: 
superadmin
sup3rdup3rs3cr3tp4ssword!
Oh, it's you! Here is your flag: %s
Hi, %s! Nice to meet you!
```

I see a password and username. Lets try running the binary and see if that works:

```bash
└─$ ./login 
Hi there! Please log in.
Username: superadmin
Password: sup3rdup3rs3cr3tp4ssword!
Oh, it's you! Here is your flag: wack{h0w_d1d_y0u_f1gur3_th4t_0ut??}
```

# Flag

```
wack{h0w_d1d_y0u_f1gur3_th4t_0ut??}
```