#include "out.h"



int _init(EVP_PKEY_CTX *ctx)

{
  int iVar1;
  
  iVar1 = __gmon_start__();
  return iVar1;
}



void FUN_00401020(void)

{
                    // WARNING: Treating indirect jump as call
  (*(code *)(undefined *)0x0)();
  return;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int putchar(int __c)

{
  int iVar1;
  
  iVar1 = putchar(__c);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int strncmp(char *__s1,char *__s2,size_t __n)

{
  int iVar1;
  
  iVar1 = strncmp(__s1,__s2,__n);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int puts(char *__s)

{
  int iVar1;
  
  iVar1 = puts(__s);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

size_t fread(void *__ptr,size_t __size,size_t __n,FILE *__stream)

{
  size_t sVar1;
  
  sVar1 = fread(__ptr,__size,__n,__stream);
  return sVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int fclose(FILE *__stream)

{
  int iVar1;
  
  iVar1 = fclose(__stream);
  return iVar1;
}



void __stack_chk_fail(void)

{
                    // WARNING: Subroutine does not return
  __stack_chk_fail();
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int printf(char *__format,...)

{
  int iVar1;
  
  iVar1 = printf(__format);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int fgetc(FILE *__stream)

{
  int iVar1;
  
  iVar1 = fgetc(__stream);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

uint alarm(uint __seconds)

{
  uint uVar1;
  
  uVar1 = alarm(__seconds);
  return uVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

size_t strcspn(char *__s,char *__reject)

{
  size_t sVar1;
  
  sVar1 = strcspn(__s,__reject);
  return sVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int memcmp(void *__s1,void *__s2,size_t __n)

{
  int iVar1;
  
  iVar1 = memcmp(__s1,__s2,__n);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

char * fgets(char *__s,int __n,FILE *__stream)

{
  char *pcVar1;
  
  pcVar1 = fgets(__s,__n,__stream);
  return pcVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

__sighandler_t signal(int __sig,__sighandler_t __handler)

{
  __sighandler_t p_Var1;
  
  p_Var1 = signal(__sig,__handler);
  return p_Var1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int fflush(FILE *__stream)

{
  int iVar1;
  
  iVar1 = fflush(__stream);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int setvbuf(FILE *__stream,char *__buf,int __modes,size_t __n)

{
  int iVar1;
  
  iVar1 = setvbuf(__stream,__buf,__modes,__n);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

FILE * fopen(char *__filename,char *__modes)

{
  FILE *pFVar1;
  
  pFVar1 = fopen(__filename,__modes);
  return pFVar1;
}



void FUN_00401240(int param_1)

{
                    // WARNING: Subroutine does not return
  exit(param_1);
}



void processEntry _start(undefined8 param_1,undefined8 param_2)

{
  undefined auStack_8 [8];
  
  __libc_start_main(main,param_2,&stack0x00000008,0,0,param_1,auStack_8);
  do {
                    // WARNING: Do nothing block with infinite loop
  } while( true );
}



void _dl_relocate_static_pie(void)

{
  return;
}



// WARNING: Removing unreachable block (ram,0x0040129d)
// WARNING: Removing unreachable block (ram,0x004012a7)

void deregister_tm_clones(void)

{
  return;
}



// WARNING: Removing unreachable block (ram,0x004012df)
// WARNING: Removing unreachable block (ram,0x004012e9)

void register_tm_clones(void)

{
  return;
}



void __do_global_dtors_aux(void)

{
  if (completed_0 == '\0') {
    deregister_tm_clones();
    completed_0 = 1;
    return;
  }
  return;
}



void frame_dummy(void)

{
  register_tm_clones();
  return;
}



void kill_on_timeout(int param_1)

{
  if (param_1 == 0xe) {
    printf("[!] Anti DoS.");
    FUN_00401240(0);
  }
  return;
}



void initialize(void)

{
  long in_FS_OFFSET;
  char local_1d;
  int local_1c;
  FILE *local_18;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_18 = fopen("/dev/urandom","r");
  local_1c = 0;
  while (local_1c < 0x15) {
    fread(&local_1d,1,1,local_18);
    if (('\x1f' < local_1d) && (local_1d < '|')) {
      admin_password[local_1c] = local_1d;
      local_1c = local_1c + 1;
    }
  }
  fclose(local_18);
  setvbuf(stdout,(char *)0x0,2,0);
  setvbuf(stdin,(char *)0x0,2,0);
  setvbuf(stderr,(char *)0x0,2,0);
  signal(0xe,kill_on_timeout);
  alarm(0x3c);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    // WARNING: Subroutine does not return
    __stack_chk_fail();
  }
  return;
}



undefined8 FLAG(void)

{
  int iVar1;
  size_t sVar2;
  long in_FS_OFFSET;
  undefined8 uStack_60;
  undefined8 uStack_58;
  undefined4 uStack_50;
  undefined8 uStack_40;
  undefined8 uStack_38;
  undefined4 uStack_30;
  long lStack_28;
  code *pcStack_20;
  char local_11;
  FILE *local_10;
  
  if (authorized != '\0') {
    pcStack_20 = (code *)0x4014c6;
    local_10 = fopen("./flag.txt","r");
    if (local_10 != (FILE *)0x0) goto LAB_004014f5;
    pcStack_20 = (code *)0x4014e0;
    puts("Could not locate flag file! Contact admins to find it!");
    pcStack_20 = (code *)0x4014ea;
    FUN_00401240(1);
    do {
      pcStack_20 = (code *)0x4014f5;
      putchar((int)local_11);
LAB_004014f5:
      pcStack_20 = (code *)0x401501;
      iVar1 = fgetc(local_10);
      local_11 = (char)iVar1;
    } while (local_11 != -1);
    pcStack_20 = (code *)0x401514;
    putchar(10);
    pcStack_20 = (code *)0x40151e;
    FUN_00401240(0);
  }
  pcStack_20 = (code *)0x40152d;
  puts("Sorry not authorized to read the flag!");
  pcStack_20 = main;
  FUN_00401240(1);
  lStack_28 = *(long *)(in_FS_OFFSET + 0x28);
  uStack_60 = 0;
  uStack_58 = 0;
  uStack_50 = 0;
  uStack_40 = 0;
  uStack_38 = 0;
  uStack_30 = 0;
  pcStack_20 = (code *)&stack0xfffffffffffffff8;
  puts(
      "This system is for authorized use only. Unauthorized access will result in immediate disconnection!"
      );
  printf("Username: ");
  fgets((char *)&uStack_40,0x14,stdin);
  putchar(10);
  fflush(stdout);
  sVar2 = strcspn((char *)&uStack_40,"\n");
  *(undefined *)((long)&uStack_40 + sVar2) = 0;
  printf((char *)&uStack_40);
  printf("@coolbox\'s password: ");
  fgets((char *)&uStack_60,200,stdin);
  putchar(10);
  iVar1 = strncmp((char *)&uStack_40,"admin",5);
  if (iVar1 == 0) {
    iVar1 = memcmp(admin_password,&uStack_60,0x14);
    if (iVar1 == 0) {
      authorized = '\x01';
      goto LAB_00401691;
    }
  }
  printf("DISCONNECTED!");
LAB_00401691:
  if (lStack_28 != *(long *)(in_FS_OFFSET + 0x28)) {
                    // WARNING: Subroutine does not return
    __stack_chk_fail();
  }
  return 0;
}



undefined8 main(void)

{
  int iVar1;
  size_t sVar2;
  long in_FS_OFFSET;
  undefined8 local_48;
  undefined8 local_40;
  undefined4 local_38;
  undefined8 local_28;
  undefined8 local_20;
  undefined4 local_18;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_48 = 0;
  local_40 = 0;
  local_38 = 0;
  local_28 = 0;
  local_20 = 0;
  local_18 = 0;
  puts(
      "This system is for authorized use only. Unauthorized access will result in immediate disconnection!"
      );
  printf("Username: ");
  fgets((char *)&local_28,0x14,stdin);
  putchar(10);
  fflush(stdout);
  sVar2 = strcspn((char *)&local_28,"\n");
  *(undefined *)((long)&local_28 + sVar2) = 0;
  printf((char *)&local_28);
  printf("@coolbox\'s password: ");
  fgets((char *)&local_48,200,stdin);
  putchar(10);
  iVar1 = strncmp((char *)&local_28,"admin",5);
  if (iVar1 == 0) {
    iVar1 = memcmp(admin_password,&local_48,0x14);
    if (iVar1 == 0) {
      authorized = 1;
      goto LAB_00401691;
    }
  }
  printf("DISCONNECTED!");
LAB_00401691:
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    // WARNING: Subroutine does not return
    __stack_chk_fail();
  }
  return 0;
}
abcdefghijklmnopqrstuvwxyzABCDEFadminGHIJKLMNOPQRSTUVWXY < stack smashing error..
abcdefghijklmnopqrstuvwxyzABCDEFadmin111111111111111111
```


void _fini(void)

{
  return;
}



