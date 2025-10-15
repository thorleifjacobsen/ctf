make# Bønnsipp

Our professor told us to implement a compression algorithm. Of course, we chose bzip2, and made a minimal implementation of the core principles of bzip2.
When testing our finished assignment, we accidentally ran `./compress decompress.c decompress.c`, overwriting the decompression source code.

We still need to submit our assignment, can you somehow recover our decompressor, for example by first writing your own?

## Practical information

### Building

To build "compress" and "decompress", you just need a "normal" C compiler like GCC or Clang, and optionally GNU Make.
You should not need any libraries outside the c standard libraries.
If building manually without GNU Make, see the compiler flags in the Makefile.

#### With GNU Make

Install gcc, glibc and make.
On Debian Linux and related distros: `sudo apt install build-essential`.

In the `./src` directory, there is a `Makefile`, allowing you to compile the project like this:
```
cd src
make compress
make decompress
```

### Sample
We have included the files `sample-file.txt` and `samle-file.txt.wackbzip2`, generated with the command `./compress sample-file.txt sample-file.txt.wackbzip2`.

