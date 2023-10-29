#include <stdlib.h>
#include <stdio.h>

void main() {
    setbuf(stdout, NULL);
    unsigned int num1;
    unsigned int num2;
    char str3[64];

    puts("Welcome, please set some variables.");
    puts("first number: ");
    scanf("%d", &num1);
    puts("another number: ");
    scanf("%d", &num2);

    if (num1 > 1000 || num2 > 1000) {
        puts("I can't handle numbers larger than 1000!");
        exit(0);
    }

    puts("and then a string: ");
    scanf("%s", &str3);
3405691582 - 3735928559

    if (num1 == 0xcafebabe && num2 == 0xdeadbeef) {
        puts("Congratulations! Here is your flag: ");
        system("cat flag.txt");
    } else {
        printf("num1: %d, num2: %d, string: %s\n", num1, num2, str3);
        puts("Thank you for your service");
    }
    
    exit(0);
}
