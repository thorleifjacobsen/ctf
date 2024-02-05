
void FUN_00101840(long param_1,long param_2,long param_3,long param_4)

{
  int local_c;
  
  for (local_c = 0; local_c < param_2; local_c = local_c + 1) {
    *(byte *)(param_1 + local_c) =
         *(byte *)(param_3 + (long)local_c % param_4) ^ *(byte *)(param_1 + local_c);
  }
  return;
}

