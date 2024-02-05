
undefined8 main(undefined8 param_1,char **param_2)

{
  int iVar1;
  undefined8 uVar2;
  undefined *puVar3;
  size_t sVar4;
  int local_8c;
  undefined local_88 [24];
  __off_t local_70;
  size_t local_68;
  char *local_48;
  undefined4 local_3c;
  int *local_38;
  char *local_30;
  long local_28;
  int local_1c;
  char *local_18;
  long local_10;
  
  local_18 = *param_2;
  iVar1 = elf_version(1);
  if (iVar1 == 0) {
    uVar2 = elf_errmsg(0xffffffff);
    fprintf(stderr,"ELF library initialization failed: %s\n",uVar2);
  }
  else {
    local_1c = open(local_18,0);
    if (local_1c < 0) {
      perror("open");
    }
    else {
      local_28 = elf_begin(local_1c,1,0);
      if (local_28 == 0) {
        uVar2 = elf_errmsg(0xffffffff);
        fprintf(stderr,"elf_begin: %s\n",uVar2);
        close(local_1c);
      }
      else {
        local_10 = 0;
        local_30 = param_2[1];
        while (local_10 = elf_nextscn(local_28,local_10), local_10 != 0) {
          puVar3 = (undefined *)gelf_getshdr(local_10,local_88);
          if (puVar3 != local_88) {
            uVar2 = elf_errmsg(0xffffffff);
            fprintf(stderr,"gelf_getshdr() failed: %s\n",uVar2);
            elf_end(local_28);
            close(local_1c);
            return 1;
          }
          local_38 = (int *)malloc(local_68);
          if (local_38 == (int *)0x0) {
            perror("malloc");
            elf_end(local_28);
            close(local_1c);
            return 1;
          }
          sVar4 = pread(local_1c,local_38,local_68,local_70);
          if (sVar4 != local_68) {
            perror("pread");
            free(local_38);
            elf_end(local_28);
            close(local_1c);
            return 1;
          }
          local_3c = 0xeefeaafa;
          if (*local_38 == -0x11015506) {
            local_8c = local_38[1];
            local_48 = (char *)xor(local_38 + 2,local_68 - 8,&local_8c);
            puts(local_48);
            free(local_38);
            free(local_48);
            elf_end(local_28);
            close(local_1c);
            return 0;
          }
          free(local_38);
        }
        fprintf(stderr,"Section not found: %s\n",local_30);
        elf_end(local_28);
        close(local_1c);
      }
    }
  }
  return 1;
}

