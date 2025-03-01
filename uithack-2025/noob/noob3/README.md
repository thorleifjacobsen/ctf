# noob3

Third time's the charm. And this time they even remembered to delete the flag so you cannot take it back.
It should be too late, but who says `history` can't be changed?
You can connect to their server with the following command `ssh noob3@uithack-2.td.org.uit.no -p 6002`
The password is the flag in the previous noob challenge.
Use command `exit` to disconnect from the server when you are done.


# Writeup

```bash
noob3@3cca5d77d453:~$ ls -lah
total 20K
drwxr-xr-x 1 root root 4.0K Feb 23 17:07 .
drwxr-xr-x 1 root root 4.0K Feb 23 17:07 ..
-rwxr--r-- 1 root root  588 Jan 22 16:23 .bash_history
noob3@3cca5d77d453:~$ cat .bash_history 
hydra -l ubuntu -p xkTfqSsLVesmHh4 -M domains.txt ssh
knockpy
ls
rm knockpy_report/
rm -rf knockpy_report/
zip2john backup.zip > hashes
cat hashes
john -wordlist=/usr/share/wordlists/rockyou.txt hashes
UiTHack25{Nev3r_f0rg3771_ctrl_shift_del} > flag.txt
nmap -sC -sV -v 10.129.98.20
ping 10.129.98.20
ifconfig
ls
cd ghidra
./main
chmod +x main
./main
ls
code  main_func.c
./main
chmod +x main
./main
chmod +x main
./main
chmod +x main
./main
ghidra
ls
rm main.go
rm main
ls
build main.go
go build main.go
./main
go build main.go
ls
./main
go build main.go
ls
gcc --help
ls
cd
rm flag.txt
noob3@3cca5d77d453:~$ 
```


# Flag

```
UiTHack25{Nev3r_f0rg3771_ctrl_shift_del}
```