#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void ignore_me(){
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
}

void timeout(int signal){
  if (signal == SIGALRM){
    printf("You timed out!\n");
    _exit(0);
  }
}

void ignore_me_timeout(){
  signal(SIGALRM, timeout);
  alarm(60);
}

void banner(){
  puts("___________                                    __         .__    .__ ");
  puts("\\__    ________    _____ _____    ____   _____/  |_  ____ |  |__ |__|");
  puts("  |    |  \\__  \\  /     \\\\__  \\  / ___\\ /  _ \\   ___/ ___\\|  |  \\|  |");
  puts("  |    |   / __ \\|  Y Y  \\/ __ \\/ /_/  (  <_> |  | \\  \\___|   Y  |  |");
  puts("  |____|  (____  |__|_|  (____  \\___  / \\____/|__|  \\___  |___|  |__|");
  puts("               \\/      \\/     \\/_____/                  \\/     \\/    ");
}

void animal(){
  puts("((...))");
  puts("( O O )");
  puts(" \\   / ");
  puts(" (`_`) \n");
}

void print_actions(){
  puts("1. Play");
  puts("2. Feed");
  puts("3. Care");
  printf(">> ");
}

void play(){
  puts("\nYou played with your pet!");
  puts("Your pet is now hungry!\n");
}

void feed(){
  char food[20];
  puts("\nWhat do you want to feed your pet?");
  printf(">> ");
  gets(food);
  printf("Your fed your pet with %s\n", food);
  puts("You pet is full\n");
  // Her vil den hente adressen fra `rip` og kjøre koden fra den adressen.
}

void print_care_options(){
  puts("1. Clean up");
  puts("2. Bathe");
  puts("3. Read a book");
  printf(">> ");
}

void care(){
  int care;
  char book[30];

  puts("\nWhat do you want to do?");
  print_care_options();
  if(scanf("%d%*c", &care) == 0)
    exit(0);
  switch(care){
    case 1:
      puts("\nYou cleaned up after you pet!\n");
      break;
    case 2:
      puts("\nYou bathed your pet!\n");
      break;
    case 3:
      puts("\nWhich book do you want to read?");
      printf(">> ");
      gets(book);
      printf("You read %s for you pet\n", book);
      break;
    default:
      puts("Invalid option");
  }
  return;
}

int main(){
  ignore_me();
  ignore_me_timeout();

  int action;
  banner();
  puts("\nHere is your pet\n");

  while(1){
    animal();
    puts("What do you want to do?");
    print_actions();
    if(scanf("%d%*c", &action) == 0)
      exit(0);
    switch(action){
      case 1:
        play();
        break;
      case 2:
        feed();
        break;
      case 3:
        care();
        break;
      default:
        puts("Invalid option!");
        exit(0);
    }
  }
  return 0;
}
