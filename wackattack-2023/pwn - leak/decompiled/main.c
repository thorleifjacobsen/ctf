
undefined8 main(void)

{
  int iVar1;
  undefined2 local_1a;
  uint local_18;
  uint local_14;
  uint local_10;
  uint local_c;
  
  setbuf(stdout,(char *)0x0);
  local_c = 0xcafebabe;
  local_10 = 0xdeadbeef;
  local_14 = 0xc0ffee;
  local_1a = 0;
  puts("Hope you\'re having a great day!");
  puts("Please input you favorite number");
  __isoc99_scanf("%d",&local_18);
  getchar();
  puts("The numbers are:");
  printf("1: 0x%x \n2: 0x%x \n3: 0x%x \n4: 0x%x \n5: %20$p\n\n",(ulong)local_c,(ulong)local_10,
         (ulong)local_14,(ulong)local_18);
  puts("Which of these numbers was your favorite? (1-5)");
  gets((char *)&local_1a);
  iVar1 = strcmp((char *)&local_1a,"4");
  if (iVar1 == 0) {
    maybe_win();
  }
  else {
    puts("What? You really should remember your FAVORITE number!!");
  }
  return 0;
}

