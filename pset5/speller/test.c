#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

// Represents a node in a hash table
typedef struct node
{
    char* word;
    struct node *next;
}
node;

int main(void) {
    node* mynode;
    mynode->word = "Hello";
    mynode->next = NULL;
    free(mynode);
    printf("%s\n", mynode->word);
    return 0;
}
