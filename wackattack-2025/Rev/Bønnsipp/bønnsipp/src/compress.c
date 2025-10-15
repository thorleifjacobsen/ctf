#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "utils.h"

//#define DEBUG

int MAX_BLOCKSIZE = 512;
// (Huffman encoding and byte packing is done in the utils.c file)

// Run-length encoding; Encode the buffer_in into buffer_out, and return the length of buffer_out
  // Buffer out format:
  // - repeating characters are written {n, character}
  // - non-repeating characters are written {-n, character_0, character_1, ... character_n-1}
int rle(unsigned char* buffer_in, int buffer_in_length, char* buffer_out) {
  int buffer_out_length = 0;
  char count;

  int i = 0;
  while (i < buffer_in_length) {
    // If the current char is the same as the next
    if (buffer_in[i] == buffer_in[i+1]){
      // Repeating character
      count = 0;
      do {
        count++;
        i++;
      } while (buffer_in[i] == buffer_in[i-1] && i < buffer_in_length && count < 127);

      // Write the count to buffer_out, positive to indicate repeating
      buffer_out[buffer_out_length] = count;
      // Write the character to buffer_out
      buffer_out[buffer_out_length+1] = buffer_in[i-1];
      buffer_out_length += 2;

      #ifdef DEBUG
      printf("DEBUG: Repeating character %02x, count %d\n", buffer_in[i-1], count);
      #endif

    } else {
      // Non-repeating characters
      count = 0;
      while (buffer_in[i] != buffer_in[i+1] && i < buffer_in_length && count < 127) {
        count++;
        i++;
      }

      // Write the count to buffer_out, negative to indicate non-repeating
      buffer_out[buffer_out_length++] = (unsigned char)-count;
      // Write the characters to buffer_out
      memcpy(buffer_out+buffer_out_length, buffer_in+i-count, count);
      buffer_out_length += count;

      #ifdef DEBUG
      printf("DEBUG: Non-repeating characters, count %d\n", count);
      for (int j = 0; j < count; j++) {
        printf("%02x ", buffer_in[i-count+j]);
      }
      printf("\n");
      #endif
    }
  }
  return buffer_out_length;
}

// Move-to-front; Apply the move-to-front algorithm to the buffer, to prepare it for RLE/Huffman
void move_to_front(unsigned char* buffer, int length) {
  // Initialize the table
  unsigned char mtf[256];
  for (int i = 0; i < 256; i++) mtf[i] = i;

  for (int i = 0; i < length; i++) {
    unsigned char c = buffer[i];
    // Linear search for c in mtf
    int index = 0;
    while (mtf[index] != c) index++;
    buffer[i] = index;
    // Move c to the front of mtf
    memmove(mtf+1, mtf, index);
    mtf[0] = c;
  }
}

// Burrows-Wheeler; Transform the buffer using the Burrows-Wheeler algorithm
unsigned int burrows_wheeler(unsigned char* buffer, int blocksize) {
  int BW_SIZE = blocksize+1;

  // Copy the char buffer to a short buffer
  unsigned short *bw_buffer = malloc(sizeof(unsigned short) * BW_SIZE);
  for (int i = 0; i < blocksize; i++) {
    bw_buffer[i] = buffer[i];
  }

  // Set the symbol character that is always sorted last
  bw_buffer[blocksize] = 0xffff;

  //Equivalent to: char bw_matrix[BW_SIZE][BW_SIZE];
  unsigned short (*bw_matrix)[BW_SIZE] = malloc(sizeof(unsigned short[BW_SIZE][BW_SIZE]));

  // Copy the buffer to the matrix, rotated by 1 character each row
  // This can be done more efficient with a circular buffer, but this is more readable and allows a simpler sorting algorithm
  for (int i = 0; i < BW_SIZE; i++) {
    for (int j = 0; j < BW_SIZE; j++) {
      bw_matrix[i][j] = bw_buffer[(j+(BW_SIZE-i))%BW_SIZE];
    }
  }

  // compare_length and compare() is defined in utils.c
  compare_length = BW_SIZE;
  qsort(bw_matrix, BW_SIZE, BW_SIZE*sizeof(unsigned short), compare);

  // Copy the last column of the matrix back to the buffer
  for (int i = 0; i < BW_SIZE; i++)
    buffer[i] = bw_matrix[i][blocksize] & 0xff;

  // Find the index of the original string
  int stop_index = 0;
  for (int i = 0; i < BW_SIZE; i++) {
    if (bw_matrix[i][blocksize] == 0xffff) {
      stop_index = i;
      break;
    }
  }

  free(bw_matrix);
  return stop_index;
}



int main(int argc, char *argv[]) {
  printf("WackBzip2 - Taschmex/krloer\n");

  if (argc != 3 && argc != 4) {
    printf("Usage: %s <in-filename> <out-filename> [blocksize]\n", argv[0]);
    return 1;
  }
  if (argc == 4) {
    MAX_BLOCKSIZE = atoi(argv[3]);
  }

  printf("Maximum block size: %d bytes\n", MAX_BLOCKSIZE);

  FILE *inputFile = fopen(argv[1], "rb");
  if (inputFile == NULL) {
    printf("Error: Could not open file %s\n", argv[1]);
    return 1;
  }

  is_big_endian = test_big_endian();

  // Stage 1:
  // - Read the file block by block
  // - Apply the Burrows-Wheeler transform
  // - Apply move-to-front
  // - Apply run-length encoding
  // - Save the compressed blocks to a temporary file

  // Stage 2:
  // - Read the compressed blocks from the temporary file
  // - Generate the Huffman tree
  // - Read the file again
  // - Encode each character using the Huffman tree
  // - Write the bits to the output file

  FILE *tempFile = tmpfile();
  if (tempFile == NULL) {
    printf("Error: Could not create temporary file\n");
    return 1;
  }

  unsigned char* buffer = malloc((MAX_BLOCKSIZE+1)*sizeof(unsigned char));
  char* rle_buffer = malloc((MAX_BLOCKSIZE*2)*sizeof(char));

  int blocksize = 0;
  unsigned long compressed_file_size = 0;

  // While there are still blocks to read, read a block of maximum size MAX_BLOCKSIZE
  while ((blocksize = fread(buffer, sizeof(unsigned char), MAX_BLOCKSIZE, inputFile)) != 0) {
    #ifdef DEBUG
    printf("DEBUG: Reading block of size %d\n", blocksize);
    #endif

    // Apply the Burrows-Wheeler transform
    unsigned int stop_index = burrows_wheeler(buffer, blocksize);
    // Write the stop index to the temporary file
    if (is_big_endian) stop_index = __builtin_bswap32(stop_index);
    fwrite(&stop_index, sizeof(unsigned int), 1, tempFile);
    compressed_file_size += sizeof(unsigned int);

    #ifdef DEBUG
    printf("BW: %.*s\n", blocksize+1, buffer);
    for (int i = 0; i < blocksize+1; i++) {
      printf("%02x ", (unsigned char) buffer[i]);
    }
    printf("\n");
    #endif

    // Apply move-to-front
    move_to_front(buffer, blocksize+1);

    #ifdef DEBUG
    printf("MTF: ");
    for (int i = 0; i < blocksize+1; i++) {
      printf("%02x ", (unsigned char) buffer[i]);
    }
    printf("\n");
    #endif

    // Apply run-length encoding
    int rle_length = rle(buffer, blocksize+1, rle_buffer);

    #ifdef DEBUG
    printf("RLE: ");
    for (int i = 0; i < rle_length; i++) {
      printf("%02x ", (unsigned char)rle_buffer[i]);
    }
    printf("\n");
    #endif

    // Write the compressed block to the temporary file
    #ifdef DEBUG
    printf("DEBUG: Writing temp block of size %d\n", rle_length);
    #endif

    fwrite(rle_buffer, sizeof(char), rle_length, tempFile);
    compressed_file_size += rle_length;
  }

  unsigned long input_file_size = ftell(inputFile);
  printf("Input file size: %ld bytes\n", input_file_size);

  free(buffer);
  free(rle_buffer);
  fclose(inputFile);

  rewind(tempFile);

  // Stage 2

  unsigned char* tempfile_buffer = malloc(MAX_BLOCKSIZE*sizeof(unsigned char));
  int freq[256];
  memset(freq, 0, 256*sizeof(int));
  // Read the temporary file byte by byte and generate the frequency table
  while ((blocksize = fread(tempfile_buffer, sizeof(unsigned char), MAX_BLOCKSIZE, tempFile)) != 0) {
    for (int i = 0; i < blocksize; i++) {
      freq[tempfile_buffer[i]]++;
    }
  }

  rewind(tempFile);

  // Open the output file
  FILE *outputFile = fopen(argv[2], "wb");
  if (outputFile == NULL) {
    printf("Error: Could not open file %s\n", argv[2]);
    return 1;
  }

  // Write the number of bytes in the compressed file after LRE, MTF and BW, but before Huffman
  if (is_big_endian)
      compressed_file_size = __builtin_bswap64(compressed_file_size);
  fwrite(&compressed_file_size, sizeof(unsigned long), 1, outputFile);
  struct fileWriter writer = new_file_writer(outputFile);

  // Create the Huffman tree
  // All internal workings are abstracted away in utils.c
  // This function will use the frequency table to generate a huffman tree, save the tree to the output file and return a table of bit codes
  char **hfm_table = hfm_get_compression_dict(freq, &writer);

  #ifdef DEBUG
  printf("DEBUG: Huffman tree bit cdes:\n");
  for (int i = 0; i < 256; i++) {
    if (hfm_table[i] != NULL) {
      printf("%02x: ", i);
      for (int j = 0; j < hfm_table[i][0]; j++) {
        printf("%d", hfm_table[i][j+1]);
      }
      printf("\n");
    }
  }
  #endif

  // Write the compressed blocks to the output file
  while ((blocksize = fread(tempfile_buffer, sizeof(unsigned char), MAX_BLOCKSIZE, tempFile)) != 0) {
    // Encode each character using the Huffman tree
    for (int i = 0; i < blocksize; i++) {
      write_bits(&writer, hfm_table[tempfile_buffer[i]]);
    }
  }
  free(tempfile_buffer);

  // Flush the buffer
  flush_writer(&writer);

  unsigned long output_file_size = ftell(outputFile);
  printf("Output file size: %ld bytes\n", output_file_size);

  fclose(tempFile);
  fclose(outputFile);

  return 0;
}
