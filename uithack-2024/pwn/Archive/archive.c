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

int main(){
    ignore_me();
    ignore_me_timeout();

    char flag[64];
    char buffer[30];

    FILE *f = fopen("flag.txt", "r");
    fgets(flag, 64, f);
    fclose(f);

    puts("What book do you want to read?");
    fgets(buffer, 30, stdin);
    printf(buffer);

    return 0;
}