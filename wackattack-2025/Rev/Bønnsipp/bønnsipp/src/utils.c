#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "utils.h"

#define BITWISE_FILE_WRITER_BUFFER_SIZE 1024

int compare_length = 0;
// Compare arrays of shorts
int compare(const void *a, const void *b) {
  unsigned short *a1 = (unsigned short*)a;
  unsigned short *b1 = (unsigned short*)b;

  for (int i = 0; i < compare_length; i++) {
    if (a1[i] < b1[i]) return -1;
    if (a1[i] > b1[i]) return 1;
  }
  return 0;
}

// Check the endianness of the system
char is_big_endian = -1;
char test_big_endian(void) {
  volatile unsigned int i=0x01234567;
  return (*((unsigned char*)(&i))) == 0x67;
}

// == Huffman Encoding ==

struct hfm_heap {
  int size;
  int capacity;
  struct hfm_node** array;
};

// Initialize a new node with a given character and frequency
struct hfm_node* new_node(unsigned char c, int freq) {
  struct hfm_node* node = (struct hfm_node*) malloc(sizeof(struct hfm_node));
  node->c = c;
  node->freq = freq;
  node->left = NULL;
  node->right = NULL;
  return node;
}

// Initialize a new heap with a given capacity
struct hfm_heap* new_heap(int capacity) {
  struct hfm_heap* heap = (struct hfm_heap*) malloc(sizeof(struct hfm_heap));
  heap->size = 0;
  heap->capacity = capacity;
  heap->array = (struct hfm_node**) malloc(heap->capacity * sizeof(struct hfm_node*));
  return heap;
}

// combine two nodes into one, and insert it into the heap
void hfm_combine(struct hfm_heap* heap, int indexa, int indexb) {
  struct hfm_node* nodea = heap->array[indexa];
  struct hfm_node* nodeb = heap->array[indexb];
  struct hfm_node* combined = new_node(0, nodea->freq + nodeb->freq);
  combined->left = nodea;
  combined->right = nodeb;
  heap->array[indexa] = combined;
  heap->array[indexb] = heap->array[heap->size-1];
  heap->size--;
}

// Take an array of nodes and organize a min-heap / huffman tree
void hfm_build(struct hfm_heap* heap) {
  while (heap->size > 1) {
    // While there is more than one element, find the two smallest elements and combine them
    int min_idx_a = 0;
    int min_idx_b = 1;

    for (int i = 2; i < heap->size; i++) {
      if (heap->array[i]->freq < heap->array[min_idx_a]->freq) {
        min_idx_b = min_idx_a;
        min_idx_a = i;
      } else if (heap->array[i]->freq < heap->array[min_idx_b]->freq) {
        min_idx_b = i;
      }
    }
    hfm_combine(heap, min_idx_a, min_idx_b);
  }
}

// Print the huffman tree, visual only
void hfm_print(struct hfm_node* node, int depth) {
  if (node->left == NULL && node->right == NULL) {
    printf("%*c %02x (%d)\n", depth, depth, node->c, node->freq);
  } else {
    printf("%*c (%d)\n", depth, 0, node->freq);
    hfm_print(node->left, depth+1);
    hfm_print(node->right, depth+1);
  }
}

void hfm_free(struct hfm_node* node) {
  if (node->left != NULL) {
    hfm_free(node->left);
  }
  if (node->right != NULL) {
    hfm_free(node->right);
  }

  free(node);
}

// Create a huffman tree from a frequencey table; unsigned char[256]
struct hfm_node *hfm_create_tree(int *frequency_table) {
  // Create a heap of nodes
  struct hfm_heap* heap = new_heap(256);
  for (int i = 0; i < 256; i++) {
    if (frequency_table[i] > 0) {
      heap->array[heap->size++] = new_node((unsigned char)i, frequency_table[i]);
    }
  }

  // Build the huffman tree
  hfm_build(heap);

  struct hfm_node* root = heap->array[0];
  // TODO:
  // free(heap->array);
  // free(heap);
  return root;
}

// Recursively traverse the tree and assign bit codes(0=left, 1=right) to each character
void hfm_find_bits(struct hfm_node* node, char **bitsDict, int bit_length, int bits) {
  if (node->left == NULL && node->right == NULL) {
    // We have reached a leaf node, assign the bit code to the character
    // "0100" -> {4, 0, 1, 0, 0}
    bitsDict[node->c] = (char*) malloc((bit_length+1) * sizeof(char));
    bitsDict[node->c][0] = bit_length;
    for (int i = 0; i < bit_length; i++)
      bitsDict[node->c][i+1] = (bits >> (bit_length-i-1)) & 1;

  } else {
    hfm_find_bits(node->left, bitsDict, bit_length+1, (bits << 1) | 0);
    hfm_find_bits(node->right, bitsDict, bit_length+1, (bits << 1) | 1);
  }
}

// Write the huffman tree to the file, as described in https://stackoverflow.com/a/759766
void hfm_write_to_file(struct hfm_node* tree, struct fileWriter *writer) {
  char bits[10];
  struct hfm_node *node = tree;
  if (node->left == NULL && node->right == NULL) {
    // Leaf node, write 1 bit and the character
    bits[0] = 9;
    bits[1] = 1;
    for (int i = 0; i < 8; i++)
      bits[i+2] = (node->c >> (7-i)) & 1;

    write_bits(writer, bits);
  } else {
    // Non-leaf node, write 0 bit and traverse the tree
    bits[0] = 1;
    bits[1] = 0;
    write_bits(writer, bits);
    hfm_write_to_file(node->left, writer);
    hfm_write_to_file(node->right, writer);
  }
}

// Load the huffman tree from the file as described in hfm_write_to_file
struct hfm_node *hfm_load_from_file(struct fileReader *reader) {
  unsigned char bit = read_bit(reader);
  if (bit == 1) {
    // Leaf node
    unsigned char c = 0;
    for (int i = 0; i < 8; i++) {
      c <<= 1;
      c |= read_bit(reader);
    }
    return new_node(c, 0);
  } else {
    // Non-leaf node
    struct hfm_node *left = hfm_load_from_file(reader);
    struct hfm_node *right = hfm_load_from_file(reader);
    struct hfm_node *node = new_node(0, 0);
    node->left = left;
    node->right = right;
    return node;
  }

}

// Returns a dictionary of bit codes for each character
// The "dictionary" is a 256 element array of char pointers
// Each element in the array is on the form {bit_length, bit0, bit1, ... bitN}
char **hfm_get_compression_dict(int *frequency_table, struct fileWriter *writer) {
  struct hfm_node* tree = hfm_create_tree(frequency_table);
  // Populate the bitsDict
  char** bitsDict = (char**) malloc(256 * sizeof(char*));
  memset(bitsDict, 0, 256 * sizeof(char*));
  hfm_find_bits(tree, bitsDict, 0, 0);

  hfm_write_to_file(tree, writer);

  // All important data is now in bitsDict, remember to free the tree
  hfm_free(tree);

  return bitsDict;
}


// == File writer ==

struct fileWriter new_file_writer(FILE *file) {
  // FILE* file = fopen(filename, "wb");
  struct fileWriter writer;
  writer.file = file;
  writer.buffer = 0;
  writer.buffer_bits = 0;
  writer.write_count = 0;

  return writer;
}

// Write the buffer to the file
void flush_writer(struct fileWriter* writer) {
  if (writer->buffer_bits == 0) return;

  int padding_bits = (8*sizeof(unsigned int)) - writer->buffer_bits;
  writer->buffer <<= padding_bits;

  #ifdef DEBUG
  if (padding_bits > 0)
    printf("DEBUG: Padding buffer with %d bits\n", padding_bits);
  #endif

  if (is_big_endian)
    writer->buffer = __builtin_bswap32(writer->buffer);

  fwrite((const void*) &(writer->buffer), sizeof(writer->buffer), 1, writer->file);
  writer->buffer = 0;
  writer->buffer_bits = 0;
  writer->write_count++;
}

// Example input: {4, 0, 1, 0, 0} -> The bits 0100 are written to file
void write_bits(struct fileWriter* writer, char* bytes) {
  unsigned char bitCount = bytes[0];
  for (int i = 0; i < bitCount; i++) {
    if (writer->buffer_bits == (8*sizeof(unsigned int))) {
      flush_writer(writer);
    }
    writer->buffer <<= 1;
    writer->buffer |= bytes[1+i];
    writer->buffer_bits++;
  }
}

// File reader

struct fileReader new_file_reader(FILE *file) {
  struct fileReader reader;
  reader.file = file;
  reader.buffer = 0;
  reader.read_bits = 0;
  return reader;
}

void refresh_buffer(struct fileReader *reader) {
  fread(&reader->buffer, sizeof(unsigned int), 1, reader->file);
  if (is_big_endian)
    reader->buffer = __builtin_bswap32(reader->buffer);
  reader->read_bits = 0;
}

unsigned char read_bit(struct fileReader *reader) {
  if (reader->read_bits == sizeof(unsigned int) * 8) {
    refresh_buffer(reader);
  }
  unsigned char bit = (reader->buffer >> (31 - reader->read_bits)) & 1;
  reader->read_bits++;
  return bit;
}
