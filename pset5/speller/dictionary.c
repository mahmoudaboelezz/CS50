#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Implements a dictionary's functionality

#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char* word;
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    char* word_cpy = strdup(word);
    word_cpy[strlen(word_cpy)] = 0;
    char* tmp = word_cpy;
    for ( ; *tmp;  tmp++) *tmp = tolower(*tmp);
    node* current = table[hash(word_cpy)];
    while (current->next) {
        if (strcmp(current->word, word_cpy) == 0) {
            return true;
        }
        current = current->next;
    }
    free(word_cpy);

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Find the place the first letter of {word} has in the alphabet (0 based)
    int pos = toupper(word[0]) % 32 - 1;
    return pos;
}

// Appends a node with a string value at the end of a linked list
void append_node(node* current, char* value) {
    if (!current->word) {
        current->word = strdup(value);
        return;
    }
    while (current->next) {
        current = current->next;
    }
    current->next = malloc(sizeof(node));
    current = current->next;
    current->next = NULL;
    current->word = strdup(value);
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++) {
        table[i] = malloc(sizeof(node));
        table[i]->word = malloc(LENGTH + 1);
        table[i]->word = NULL;
        table[i]->next = NULL;
    }

    FILE* file = fopen(dictionary, "r");
    if (!file) {
        return false;
    }
    char* line = malloc(LENGTH + 1);

    // Fill hash table
    while (fgets(line, LENGTH, file)) {
        line[strlen(line) - 1] = 0;
        append_node(table[hash(line)], line);
    }

    free(line);

    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    unsigned int total = 0;
    for (int i = 0; i < N; i++) {
        node* current = table[i];
        while (current->next) {
            total++;
            current = current->next;
        }
        total++;
    }
    return total;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < N; i++) {
        node* current = table[i];
        node* tmp = NULL;
        while (current) {
            tmp = current;
            current = current->next;
            free(tmp->word);
            free(tmp);
        }
    }
    return true;
}
