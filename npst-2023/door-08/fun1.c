
/* WARNING: Function: _guard_dispatch_icall replaced with injection: guard_dispatch_icall */

uint FUN_140143dac(void)

{
  undefined8 uVar1;
  bool bVar2;
  char cVar3;
  byte bVar4;
  int iVar5;
  code **ppcVar6;
  longlong *plVar7;
  undefined8 uVar8;
  undefined8 *puVar9;
  undefined4 *puVar10;
  undefined *puVar11;
  uint unaff_EBX;
  undefined8 in_R9;
  undefined uVar12;
  
  cVar3 = __scrt_initialize_crt(1);
  if (cVar3 == '\0') {
    FUN_14014464c(7);
  }
  else {
    bVar2 = false;
    uVar12 = 0;
    bVar4 = __scrt_acquire_startup_lock();
    unaff_EBX = unaff_EBX & 0xffffff00 | (uint)bVar4;
    puVar11 = (undefined *)(ulonglong)DAT_1401bd390;
    if (DAT_1401bd390 != 1) {
      if (DAT_1401bd390 == 0) {
        DAT_1401bd390 = 1;
        iVar5 = _initterm_e(&DAT_140145670,&DAT_140145688);
        if (iVar5 != 0) {
          return 0xff;
        }
        puVar11 = &DAT_140145650;
        _initterm(&DAT_140145650,&DAT_140145668);
        DAT_1401bd390 = 2;
      }
      else {
        bVar2 = true;
        uVar12 = 1;
      }
      __scrt_release_startup_lock((ulonglong)puVar11 & 0xffffffffffffff00 | (ulonglong)bVar4);
      ppcVar6 = (code **)FUN_140144634();
      if ((*ppcVar6 != (code *)0x0) && (cVar3 = FUN_1401443cc(ppcVar6), cVar3 != '\0')) {
        (**ppcVar6)(0,2,0,in_R9,uVar12);
      }
      plVar7 = (longlong *)FUN_14014463c();
      if ((*plVar7 != 0) && (cVar3 = FUN_1401443cc(plVar7), cVar3 != '\0')) {
        _register_thread_local_exe_atexit_callback(*plVar7);
      }
      uVar8 = _get_initial_narrow_environment();
      puVar9 = (undefined8 *)__p___argv();
      uVar1 = *puVar9;
      puVar10 = (undefined4 *)__p___argc();
      unaff_EBX = FUN_140075170(*puVar10,uVar1,uVar8);
      cVar3 = FUN_1401447a0();
      if (cVar3 != '\0') {
        if (!bVar2) {
          _cexit();
        }
        __scrt_uninitialize_crt(1,0);
        return unaff_EBX;
      }
      goto LAB_140143f18;
    }
  }
  FUN_14014464c(7);
LAB_140143f18:
                    /* WARNING: Subroutine does not return */
  exit(unaff_EBX);
}


