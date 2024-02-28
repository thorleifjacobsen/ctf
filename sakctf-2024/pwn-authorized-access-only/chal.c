
undefined8 main(void)

{
  int iVar1;
  undefined8 local_48;
  undefined8 local_40;
  undefined4 local_38;
  undefined8 local_28;
  undefined8 local_20;
  undefined4 local_18;
  char local_12;
  char local_11;
  FILE *local_10;
  
  local_12 = '\0';
  local_28 = 0;
  local_20 = 0;
  local_18 = 0;
  local_48 = 0;
  local_40 = 0;
  local_38 = 0;
  initialize();
  puts(
      "This system is for authorized use only. Unauthorized access will result in immediate disconne ction!"
      );
  printf("Username: ");
  fgets((char *)&local_28,0x14,stdin);
  printf("\nPassword: ");
  fgets((char *)&local_48,200,stdin);
  putchar(10);
  iVar1 = strncmp((char *)&local_28,"admin",5);
  if (iVar1 == 0) {
    iVar1 = strncmp((char *)&local_48,"l37 m3 3n73r plz!",0x11);
    if (iVar1 == 0) {
      iVar1 = strcmp(&local_12,"true");
      if (iVar1 == 0) {
        local_10 = fopen("./flag.txt","r");
        if (local_10 == (FILE *)0x0) {
          puts("Could not locate flag file! Contact admins to find it!");
                    /* WARNING: Subroutine does not return */
          exit(1);
        }
        while( true ) {
          iVar1 = fgetc(local_10);
          local_11 = (char)iVar1;
          if (local_11 == -1) break;
          putchar((int)local_11);
        }
        putchar(10);
                    /* WARNING: Subroutine does not return */
        exit(0);
      }
    }
  }
  printf("DISCONNECTED!");
  return 0;
}

l37 m3 3n73r plz!                      true

l37 m3 3n73r plz!XXXXXXXXXXXXXXXadminXXXXXXXXXXXXXXXXXtrue