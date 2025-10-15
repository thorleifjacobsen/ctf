#ifndef BZ2UTILS
#define BZ2UTILS

extern int compare_length;
int compare(const void *a, const void *b);
extern char is_big_endian;
char test_big_endian(void);

// File writer
struct fileWriter {
    FILE* file;
    unsigned int buffer;
    short buffer_bits; // The number of bits already in the buffer
    unsigned int write_count;
};
struct fileWriter new_file_writer(FILE *file);
void flush_writer(struct fileWriter* writer);
void write_bits(struct fileWriter* writer, char* bytes);

// File reader
struct fileReader {
    FILE* file;
    unsigned int buffer;
    unsigned char read_bits;
};
struct fileReader new_file_reader(FILE *file);
void refresh_buffer(struct fileReader *reader);
unsigned char read_bit(struct fileReader *reader);

// Huffman encoding
struct hfm_node {
  unsigned char c;
  int freq;
  struct hfm_node* left;
  struct hfm_node* right;
};
char **hfm_get_compression_dict(int *frequency_table, struct fileWriter* writer);
struct hfm_node *hfm_load_from_file(struct fileReader *reader);


#endif
