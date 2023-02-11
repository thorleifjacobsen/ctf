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

void print_flag(){
  char chr;
  FILE *f = fopen("flag.txt", "r");
  chr = fgetc(f);
  while(chr != EOF){
    printf("%c", chr);
    chr = fgetc(f);
  }
  fclose(f);
}

void menu(){
  puts("How can I help you?");
  puts("1. Buy");
  puts("2. Exit");
  printf(">> ");
}

void print_items(){
  puts("\nWhat item would you like to buy?");
  puts("1. Holly wand      7g");
  puts("2. Flag            50g");
  printf(">> ");
}

int buy_amount(){
  int amount;
  puts("\nHow many would you like to buy?");
  printf(">> ");
  if(scanf("%d", &amount) == 0)
    exit(0);
  return amount;
}

int buy(int galleons){
  int item, amount;

  printf("\nYou have %dg\n", galleons);
  print_items();
  if(scanf("%d", &item) == 0)
    exit(0);

  if(item == 1){
    amount = buy_amount();
    if((galleons - 7 * amount) < 0){
      puts("Not enough galleons!\n");
      return galleons;
    }
    galleons -= 7 * amount;
    puts("\nYou have purchased the Holly wand!");
  }
  else if(item == 2){
    if((galleons - 50) < 0){
      puts("Not enough galleons!\n");
      return galleons;
    }
    galleons -= 50;
    puts("\nYou have purchased the flag!");
    print_flag();
    _exit(0);
  }
  printf("\nYou have %d galleons\n\n", galleons);
  return galleons;
}

int main(){
  ignore_me();
  ignore_me_timeout();

  int galleons = 20;
  int option = 0;

  puts("Welcome to Ollivanders");
  while(1){
    menu();
    scanf("%d", &option);
    switch(option){
      case 1:
        galleons = buy(galleons);
        break;
      case 2:
        puts("See you later!");
        exit(0);
      default:
        puts("Invalid option!");
        exit(0);
    }
  }
  return 0;
}
