#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void win() {
    char flag[100] = {0};
    FILE *fd = fopen("flag.txt", "r");
    if (!fd) {
        puts("Couldn't find a flag file");
        exit(1);
    }
    fgets(flag, 100, fd);
    puts(flag);
    exit(0);
}

int main() {
    setbuf(stdout, NULL);
    char buffer[0100];
    char secret_card[6] = "joker\0";

    puts("I have selected a playing card, there's no way you will guess what it is!");
    printf("Enter your guess: ");
    fgets(buffer, 0x100, stdin);

    if (strncmp("joker", buffer, 5) == 0) {
        puts("You're joking right? (sorry)");
        exit(0);
    }

    buffer[strcspn(buffer, "\n")] = 0;
    printf("You guessed %s, the secret card was the ... %s (hah)\n", buffer, secret_card);

    // Don't need this, but whatever
    if (strncmp(secret_card, buffer, 5) == 0) {
        win();
    }

    return 0;
}