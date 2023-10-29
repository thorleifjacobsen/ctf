#include <stdio.h>
#include <stdlib.h>

void win() {
	char flag[100] = {0};
    FILE *fd = fopen("flag.txt", "r");
    fgets(flag, 100, fd);
    puts(flag);
}

int main() {
	setbuf(stdout, NULL);
	char buf[28];
	int admin = 0;
	
	puts("Welcome to pwn!!!!");
	puts("What would you like to say? (no more than 28 characters please)");

	gets(buf);

	if (admin) {
		puts("Oh you are a ctf admin? Here you go:");
		win();
		exit(0);
	}

	puts("Thank you for your comment! Have a great day.");
	exit(0);
}
