

undefined * user_create(char *newName,undefined sessionPointer) {
  char cVar1;
  size_t nameLength;
  undefined *puVar2;
  char *pcVar3;
  
  nameLength = strlen(newName);
  cVar1 = username_valid(newName,nameLength);
  if (cVar1 == '\0') {
    puVar2 = (undefined *)0x0;
  }
  else {
    puVar2 = (undefined *)malloc(9);
    pcVar3 = strdup(newName);
    *puVar2 = sessionPointer;
    *(char **)(puVar2 + 1) = pcVar3;
  }
  return puVar2;
}







void user_free(void *param_1)

{
  if (param_1 != (void *)0x0) {
    if (*(void **)((long)param_1 + 1) != (void *)0x0) {
      free(*(void **)((long)param_1 + 1));
    }
    free(param_1);
    return;
  }
  return;
}


