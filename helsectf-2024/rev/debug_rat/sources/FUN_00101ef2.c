
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */
/* WARNING: Restarted to delay deadcode elimination for space: stack */

void FUN_00101ef2(undefined4 param_1,undefined8 param_2)

{
  long lVar1;
  FILE *pFVar2;
  int iVar3;
  ulong uVar4;
  size_t sVar5;
  char *pcVar6;
  long lVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  long in_FS_OFFSET;
  byte bVar10;
  undefined8 local_598;
  undefined4 local_58c;
  int local_588;
  int local_584;
  int local_580;
  int local_57c;
  char *local_578;
  char *local_570;
  size_t local_568;
  char *local_560;
  long local_558;
  undefined *local_550;
  FILE *local_548;
  undefined8 *local_540;
  char *local_538 [3];
  char *local_520;
  char acStack_51d [5];
  undefined8 local_518;
  undefined8 local_510;
  undefined2 local_508;
  undefined local_506;
  undefined8 local_4f8;
  undefined8 local_4f0;
  undefined8 local_4e8;
  undefined8 local_4e0;
  undefined4 local_4d8;
  undefined local_4d4;
  char local_4c8 [4];
  char local_4c4;
  char local_4c3;
  char local_4c2;
  char cStack_4c1;
  undefined6 uStack_4c0;
  undefined8 local_4ba;
  undefined8 local_4b2;
  undefined8 local_4aa;
  undefined8 local_448;
  undefined8 local_440;
  undefined8 local_438;
  undefined8 local_430;
  undefined8 local_428;
  undefined8 local_420;
  undefined8 local_418;
  undefined4 local_410;
  undefined2 local_40c;
  undefined8 local_40;
  
  bVar10 = 0;
  local_40 = *(undefined8 *)(in_FS_OFFSET + 0x28);
  local_4f8 = 0x23727d6460666d53;
  local_4f0 = 0x3330347621544352;
  local_4e8 = 0x3330343131303232;
  local_4e0 = 0x6664293331303234;
  local_4d8 = 0xb677762;
  local_4d4 = 0;
  local_518 = 0x504c243a514c4748;
  local_510 = 0x4658412055414120;
  local_508 = 0x843;
  local_506 = 0;
  DAT_00105363 = 1;
  DAT_001053a0 = &DAT_001050d8;
  local_598 = param_2;
  local_58c = param_1;
  FUN_00101750();
  FUN_00101947(&local_4f8,0x24);
  FUN_001018c6(&local_518,0x12);
  puts((char *)&local_518);
  FUN_001017e5();
LAB_0010200d:
  do {
    while( true ) {
      while( true ) {
        printf("> ");
        fgets(local_4c8,0x80,stdin);
        for (local_588 = 0; (local_588 < 0x80 && (local_4c8[local_588] != '\0'));
            local_588 = local_588 + 1) {
        }
        local_588 = local_588 + -1;
        if (local_588 == 2) break;
        if (local_588 != 4) goto LAB_00102137;
        iVar3 = strncmp(local_4c8,"HELP",4);
        if (iVar3 == 0) {
          puts((char *)&local_518);
        }
        else {
          if ((((local_4c8[2] != 'N') || (local_4c8[0] != 'H')) || (local_4c8[3] != 'T')) ||
             (local_4c8[1] != 'I')) goto LAB_00102137;
          FUN_001019de();
        }
      }
      iVar3 = strncmp(local_4c8,"LS",2);
      if (iVar3 != 0) break;
      system("/bin/ls");
    }
LAB_00102137:
    if (2 < local_588) {
      if (((local_4c8[0] == 'C') && (local_4c8[1] == 'A')) && (local_4c8[2] == 'T')) {
        if (DAT_00105280 == '\0') {
          _INIT_3();
        }
        local_538[0] = "Meow! I WISH I COULD CAT A FILE";
        local_538[1] = "ONE DAY I WILL COMPLETE MY CAT COMMAND";
        local_538[2] = "YOUR GOAL IS TO: EXEC cat /flag.txt";
        local_520 = &DAT_00105280;
        iVar3 = rand();
        local_584 = iVar3 % 3;
        if ((((local_588 == 8) && (local_4c8[3] == ' ')) && (local_4c4 == '1')) &&
           (((local_4c3 == '3' && (local_4c2 == '3')) && (cStack_4c1 == '7')))) {
          local_584 = 3;
        }
        puts(local_538[local_584]);
        goto LAB_0010200d;
      }
      FUN_00101986(local_4c8,(undefined *)((long)&stack0xfffffffffffffae0 + 3),5);
      if ((4 < local_5r88) &&
         (iVar3 = strncmp((char *)((long)&stack0xfffffffffffffae0 + 3),&DAT_001050d8,5), iVar3 == 0)
         ) {
        local_448 = 0x6672243a4e444d54;
        local_440 = 0x4145402064766d6d;
        local_438 = 0x7165706e68204555;
        local_430 = 0x236f702064636366;
        local_428 = 0x23746a6577657070;
        local_420 = 0x6820504553434753;
        local_418 = 0x747261766e207b65;
        local_410 = 0x64746b72;
        local_40c = 10;
        FUN_00101947(&local_448,0x41);
        if (local_588 == 0x26) {
          local_578 = &local_4c2;
          _DAT_00105380 = CONCAT62(uStack_4c0,CONCAT11(cStack_4c1,local_4c2));
          _DAT_00105388 = local_4ba;
          _DAT_00105390 = local_4b2;
          _DAT_00105398 = local_4aa;
          FUN_00101840(&DAT_00105380,0x20,s_HELSECTF_IS_SO_MUCH_FUN_001050c0,0x18);
          puts("OK SECRET overwrite");
        }
        else {
          puts("ERROR length mismatch");
        }
        goto LAB_0010200d;
      }
      if (((local_588 == 6) &&
          ((((local_4c8[0] != '\0' && (local_4c8[1] != '\0')) && (local_4c8[2] != '\0')) &&
           ((local_4c8[3] != '\0' && (local_4c4 != '\0')))))) && (local_4c3 != '\0')) {
        DAT_001053ac = 1;
        goto LAB_0010200d;
      }
      if ((3 < local_588) && (iVar3 = strncmp(local_4c8,"EXEC",4), iVar3 == 0)) {
        local_4c8[local_588] = '\0';
        local_588 = local_588 + -5;
        local_570 = &local_4c3;
        iVar3 = FUN_00102826(local_570);
        local_568 = (size_t)iVar3;
        if (0x80 < local_568) {
          puts("EXEC too much data");
                    /* WARNING: Subroutine does not return */
          _exit(0);
        }
        local_560 = (char *)malloc(local_568);
        local_580 = FUN_001029a7(local_570,local_560,local_568);
        if (local_580 == 0) {
          puts("EXEC malformed input");
        }
        else {
          local_560[local_568] = '\0';
          FUN_00101840(local_560,local_568,&DAT_00105380,0x20);
          iVar3 = memcmp(s_HELSECTF_IS_SO_MUCH_FUN_001050c0,local_560,0x18);
          uVar4 = local_568;
          if (iVar3 == 0) {
            local_560 = local_560 + 0x18;
            local_568 = local_568 - 0x18;
            local_558 = uVar4 - 0x19;
            uVar4 = ((local_568 * 8 + 0xf) / 0x10) * 0x10;
            for (puVar8 = &local_598;
                puVar8 != (undefined8 *)((long)&local_598 - (uVar4 & 0xfffffffffffff000));
                puVar8 = (undefined8 *)((long)puVar8 + -0x1000)) {
              *(undefined8 *)((long)puVar8 + -8) = *(undefined8 *)((long)puVar8 + -8);
            }
            lVar1 = -(ulong)((uint)uVar4 & 0xfff);
            if ((uVar4 & 0xfff) != 0) {
              *(undefined8 *)((long)puVar8 + ((ulong)((uint)uVar4 & 0xfff) - 8) + lVar1) =
                   *(undefined8 *)((long)puVar8 + ((ulong)((uint)uVar4 & 0xfff) - 8) + lVar1);
            }
            pcVar6 = local_560;
            sVar5 = local_568;
            local_550 = (undefined *)((long)puVar8 + lVar1);
            *(undefined8 *)((long)puVar8 + lVar1 + -8) = 0x1026a1;
            memcpy((undefined *)((long)puVar8 + lVar1),pcVar6,sVar5);
            pcVar6 = local_560;
            local_448 = 0;
            local_440 = 0;
            puVar9 = &local_438;
            for (lVar7 = 0x7e; lVar7 != 0; lVar7 = lVar7 + -1) {
              *puVar9 = 0;
              puVar9 = puVar9 + (ulong)bVar10 * -2 + 1;
            }
            *(undefined8 *)((long)puVar8 + lVar1 + -8) = 0x1026e7;
            local_548 = popen(pcVar6,"r");
            if (local_548 == (FILE *)0x0) {
              *(undefined8 *)((long)puVar8 + lVar1 + -8) = 0x102707;
              puts("EXEC RUN failed");
                    /* WARNING: Subroutine does not return */
              *(undefined8 *)((long)puVar8 + lVar1 + -8) = 0x102711;
              _exit(0);
            }
            *(undefined8 *)((long)puVar8 + lVar1 + -8) = 0x102720;
            puts("EXEC result:");
            while( true ) {
              pFVar2 = local_548;
              *(undefined8 *)((long)puVar8 + lVar1 + -8) = 0x102798;
              pcVar6 = fgets((char *)&local_448,0x400,pFVar2);
              pFVar2 = local_548;
              if (pcVar6 == (char *)0x0) break;
              *(undefined8 *)((long)puVar8 + lVar1 + -8) = 0x102731;
              sVar5 = strlen((char *)&local_448);
              local_57c = (int)sVar5;
              lVar7 = (long)local_57c;
              *(undefined8 *)((long)puVar8 + lVar1 + -8) = 0x10275b;
              FUN_00101840(&local_448,lVar7,&DAT_00105380,0x20);
              local_540 = &local_448;
              *(undefined8 *)((long)puVar8 + lVar1 + -8) = 0x10277d;
              FUN_00102c04(&local_448);
            }
            *(undefined8 *)((long)puVar8 + lVar1 + -8) = 0x1027ac;
            pclose(pFVar2);
            *(undefined8 *)((long)puVar8 + lVar1 + -8) = 0x1027bb;
            puts("> EXEC SUCCESS");
          }
          else {
            puts("EXEC MAGIC mismatch");
          }
        }
        goto LAB_0010200d;
      }
    }
    puts("error");
  } while( true );
}

