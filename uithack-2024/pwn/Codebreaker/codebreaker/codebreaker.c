#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <time.h>

void ignore_me(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void timeout(int signal){
    if (signal == SIGALRM)
    {
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
    fclose(f);
}

void generate_code(){
    int guesses[3] = {0};
    printf("Guess the 3 next numbers to escape!\n");
    printf("The first 4 numbers are:\n%d %d %d %d\n", rand()%34, rand()%34, rand()%34, rand()%34);

    int winning_numbers[3] = {rand()%34, rand()%34, rand()%34};
    printf("Your guess: ");
    scanf("%d %d %d", &guesses[0], &guesses[1], &guesses[2]);

    if(guesses[0] == winning_numbers[0] &&
       guesses[1] == winning_numbers[1] &&
       guesses[2] == winning_numbers[2]){
        printf("You have escaped the Xenithians!\n");
        print_flag();
    } else {
        printf("The correct numbers were: %d %d %d\n", winning_numbers[0], winning_numbers[1], winning_numbers[2]);
        printf("You were dragged back to your cell!\n");
    }
}

int main(){
    ignore_me();
    ignore_me_timeout();

    unsigned long clock = time(NULL);
    srand(clock);

    printf("You look at your watch, it shows: %lu\n", clock);
    generate_code();
    return 0;
}