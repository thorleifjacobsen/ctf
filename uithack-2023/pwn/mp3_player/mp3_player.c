#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

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

void menu(){
  puts("Welcome to my online MP3 Player!\n");
  puts("Please choose the name of the song you want to play:\n");
  puts("- Photograph - Nickelback\n- Lose Yourself - Eminem\n- Mamma Mia - ABBA");
}

void photograph(){
  puts("So you can keep me");
  puts("Inside the pocket of your ripped jeans");
  puts("Holding me closer 'til our eyes meet");
  puts("You won't ever be alone");
}

void lose_yourself(){
  puts("You better lose yourself in the music");
  puts("The moment, you own it, you better never let it go");
  puts("You only get one shot, do not miss your chance to blow");
  puts("This opportunity comes once in a lifetime");
}

void mamma_mia(){
  puts("Mamma mia, here I go again");
  puts("My my, how can I resist you?");
  puts("Mamma mia, does it show again?");
  puts("My my, just how much I've missed you");
}

void call_me_maybe(){
  char chr;
  FILE *f = fopen("flag.txt", "r");
  chr = fgetc(f);
  while(chr != EOF){
    printf("%c", chr);
    chr = fgetc(f);
  }
  fclose(f);
}

void play_song(char *song){
  if(!strcmp(song, "Photograph")){
    photograph();
  }
  else if(!strcmp(song, "Lose Yourself")){
    lose_yourself();
  }
  else if(!strcmp(song, "Mamma Mia")){
    mamma_mia();
  }
  else {
    puts("Could not play the requested song");
  }
}

int main(){
  ignore_me();
  ignore_me_timeout();

  char song[30];
  menu();
  gets(song);
  play_song(song);
  return 0;
}