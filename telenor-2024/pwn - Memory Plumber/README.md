# Memory Plumber

You're the memory plumber?! Oh thank god you're here! My memory is leaking all over the place you HAVE to HELP me!!

nc 185.125.168.82 1234

[⬇️ handout.zip](./handout.zip)

# Writeup

Opened the `leak` file in Ghidra and it seems to be running this leak function. The leak function is leaking the address of the local variable `local_88` which is 128 bytes long.

```c
void leak(void) {
  char local_88 [128];
  
  printf("LEAK OVER HERE -----------------------------> %p\nPlease help me!!!\n",local_88);
  fgets(local_88,0x100,stdin);
  return;
}
```

# Flag

```

```