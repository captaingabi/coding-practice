#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char* ltrim(char*);
char* rtrim(char*);

int parse_int(char*);

/*
 * Complete the 'noPrefix' function below.
 *
 * The function accepts STRING_ARRAY words as parameter.
 */
 
 typedef struct Node{
    bool last_character;
    struct Node *children[10];
 } node_t;

bool is_prefix(node_t *node, int idx, bool last_character){
    if(node->children[idx] == NULL) {
        node->children[idx] = malloc(sizeof(node_t));
        memset(node->children[idx], 0, sizeof(node_t));
        node->children[idx]->last_character = last_character;
        return false;
    } else if(node->children[idx]->last_character || last_character){
        return true;
    } else {
        return false;
    }
}

void noPrefix(int words_count, char** words) {
    node_t *root=malloc(sizeof(node_t));
    node_t *current = memset(root, 0, sizeof(node_t));
    
    for(int i = 0; i < words_count; i++){
        int j = 0;
        while( !(words[i][j] == '\0' || words[i][j] == '\r') ){
            int idx = words[i][j] - 'a';
            if(idx < 0 || idx > 9){
                printf("Idx %i out of bounds!\n", idx);
                exit(-1);
            }
            bool last_character = (words[i][j+1] == '\0' || words[i][j+1] == '\r');
            if(is_prefix(current, idx, last_character)) {
                printf("BAD SET\n");
                printf("%s\n", words[i]);
                return;
            }
            current = current->children[idx];
            j++;
        }

         current = root;
    }
    
    printf("GOOD SET\n");
}

int main()
{
    int n = parse_int(ltrim(rtrim(readline())));

    char** words = malloc(n * sizeof(char*));

    for (int i = 0; i < n; i++) {
        char* words_item = readline();

        *(words + i) = words_item;
    }

    noPrefix(n, words);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;

    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) {
            break;
        }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') {
            break;
        }

        alloc_length <<= 1;

        data = realloc(data, alloc_length);

        if (!data) {
            data = '\0';

            break;
        }
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';

        data = realloc(data, data_length);

        if (!data) {
            data = '\0';
        }
    } else {
        data = realloc(data, data_length + 1);

        if (!data) {
            data = '\0';
        } else {
            data[data_length] = '\0';
        }
    }

    return data;
}

char* ltrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    while (*str != '\0' && isspace(*str)) {
        str++;
    }

    return str;
}

char* rtrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    char* end = str + strlen(str) - 1;

    while (end >= str && isspace(*end)) {
        end--;
    }

    *(end + 1) = '\0';

    return str;
}

int parse_int(char* str) {
    char* endptr;
    int value = strtol(str, &endptr, 10);

    if (endptr == str || *endptr != '\0') {
        exit(EXIT_FAILURE);
    }

    return value;
}
