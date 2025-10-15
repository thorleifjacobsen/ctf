CC = gcc
CFLAGS = -Wall -Wextra -Werror -Wno-unused-result -pedantic -std=c99 -O3

all: compress decompress

clean:
	rm -f *.o compress decompress

compress.o: compress.c
	$(CC) $(CFLAGS) -c compress.c -o compress.o

decompress.o: decompress.c
	$(CC) $(CFLAGS) -c decompress.c -o decompress.o

utils.o: utils.c
	$(CC) $(CFLAGS) -c utils.c -o utils.o

compress: compress.o utils.o
	$(CC) $(CFLAGS) -o compress compress.o utils.o

decompress: decompress.o utils.o
	$(CC) $(CFLAGS) -o decompress decompress.o utils.o

