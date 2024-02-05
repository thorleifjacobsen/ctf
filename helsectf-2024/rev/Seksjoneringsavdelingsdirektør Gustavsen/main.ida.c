int __fastcall main(int argc, const char **argv, const char **envp)
{
  const char *v3; // rax
  const char *v5; // rax
  const char *v6; // rax
  ssize_t v7; // rax
  uint32_t key; // [rsp+1Ch] [rbp-84h] BYREF
  GElf_Shdr shdr; // [rsp+20h] [rbp-80h] BYREF
  char *data; // [rsp+60h] [rbp-40h]
  uint32_t magic; // [rsp+6Ch] [rbp-34h]
  char *section_data; // [rsp+70h] [rbp-30h]
  const char *target_section_name; // [rsp+78h] [rbp-28h]
  Elf *elf; // [rsp+80h] [rbp-20h]
  int fd; // [rsp+8Ch] [rbp-14h]
  const char *elf_file; // [rsp+90h] [rbp-10h]
  Elf_Scn *scn; // [rsp+98h] [rbp-8h]

  elf_file = *argv;
  if ( (unsigned int)elf_version(1LL, argv, envp) )
  {
    fd = open(elf_file, 0);
    if ( fd >= 0 )
    {
      elf = (Elf *)elf_begin((unsigned int)fd, 1LL, 0LL);
      if ( elf )
      {
        scn = 0LL;
        target_section_name = argv[1];
        while ( 1 )
        {
          scn = (Elf_Scn *)elf_nextscn(elf, scn);
          if ( !scn )
            break;
          if ( (GElf_Shdr *)gelf_getshdr(scn, &shdr) != &shdr )
          {
            v6 = (const char *)elf_errmsg(0xFFFFFFFFLL);
            fprintf(stderr, "gelf_getshdr() failed: %s\n", v6);
            elf_end(elf);
            close(fd);
            return 1;
          }
          section_data = (char *)malloc(shdr.sh_size);
          if ( !section_data )
          {
            perror("malloc");
            elf_end(elf);
            close(fd);
            return 1;
          }
          v7 = pread(fd, section_data, shdr.sh_size, shdr.sh_offset);
          if ( v7 != shdr.sh_size )
          {
            perror("pread");
            free(section_data);
            elf_end(elf);
            close(fd);
            return 1;
          }
          magic = -285299974;
          if ( *(_DWORD *)section_data == -285299974 )
          {
            key = *((_DWORD *)section_data + 1);
            data = xor(section_data + 8, shdr.sh_size - 8, (char *)&key);
            puts(data);
            free(section_data);
            free(data);
            elf_end(elf);
            close(fd);
            return 0;
          }
          free(section_data);
        }
        fprintf(stderr, "Section not found: %s\n", target_section_name);
        elf_end(elf);
        close(fd);
        return 1;
      }
      else
      {
        v5 = (const char *)elf_errmsg(0xFFFFFFFFLL);
        fprintf(stderr, "elf_begin: %s\n", v5);
        close(fd);
        return 1;
      }
    }
    else
    {
      perror("open");
      return 1;
    }
  }
  else
  {
    v3 = (const char *)elf_errmsg(0xFFFFFFFFLL);
    fprintf(stderr, "ELF library initialization failed: %s\n", v3);
    return 1;
  }
}