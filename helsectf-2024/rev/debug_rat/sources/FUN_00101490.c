
void FUN_00101490(int param_1)

{
  long lVar1;
  undefined *puVar2;
  ulong uVar3;
  undefined *puVar4;
  long in_FS_OFFSET;
  undefined auStack_68 [12];
  int local_5c;
  long local_50;
  undefined *local_48;
  long local_40;
  
  puVar4 = auStack_68;
  local_5c = param_1;
  local_40 = *(long *)(in_FS_OFFSET + 0x28);
  if (param_1 == 0xe) {
    DAT_001053a8 = DAT_001053a8 + 1;
  }
  if (((int)DAT_00105361 ^ DAT_001053b0 ^ DAT_001050e0) != (uint)(DAT_001050e4 == 0)) {
    FUN_0010143c();
  }
  if (0xe < DAT_001053a8) {
    puts("INTRUDER! Your hacking was notified!");
                    /* WARNING: Subroutine does not return */
    _exit(0);
  }
  if (DAT_001053ac == 1) {
    local_50 = (long)DAT_00105054 + -1;
    uVar3 = (((long)DAT_00105054 * 8 + 0xfU) / 0x10) * 0x10;
    for (; puVar4 != auStack_68 + -(uVar3 & 0xfffffffffffff000); puVar4 = puVar4 + -0x1000) {
      *(undefined8 *)(puVar4 + -8) = *(undefined8 *)(puVar4 + -8);
    }
    lVar1 = -(ulong)((uint)uVar3 & 0xfff);
    if ((uVar3 & 0xfff) != 0) {
      *(undefined8 *)(puVar4 + ((ulong)((uint)uVar3 & 0xfff) - 8) + lVar1) =
           *(undefined8 *)(puVar4 + ((ulong)((uint)uVar3 & 0xfff) - 8) + lVar1);
    }
    local_48 = puVar4 + lVar1;
    *(undefined8 *)(puVar4 + lVar1 + -8) = 0x101610;
    FUN_00101ea3(s_eibb#ubww79%\KfqappZbKgZAd`n_00105020,(long)puVar4 + lVar1,DAT_00105054);
    puVar2 = local_48;
    *(undefined8 *)(puVar4 + lVar1 + -8) = 0x101628;
    FUN_001013e9(puVar2,(long)DAT_00105054);
    DAT_001053ac = 0;
  }
  alarm(2);
  if (local_40 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

