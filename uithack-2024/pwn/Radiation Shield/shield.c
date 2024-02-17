#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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

void print_flag(){
    char chr;
    FILE *f = fopen("flag.txt", "r");
    chr = fgetc(f);
    while (chr != EOF){
        printf("%c", chr);
        chr = fgetc(f);
    }
    printf("\n");
    fclose(f);
}

void shield_control(){
    char shield_level[10] = "medium";
    char shield_status[10] = {0};

    printf("New shield status:\n");
    fgets(shield_status, 20, stdin);

    printf("Shield status: %s\n", shield_status);
    printf("Shield level: %s\n", shield_level);

    if(strncmp(shield_level, "maximum", 7) == 0){
        print_flag();
    }
}

int main(){
    ignore_me();
    ignore_me_timeout();

    shield_control();
    return 0;
}