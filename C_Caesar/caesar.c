#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>


int main(int argc, string argv[])
{
    string key = argv[1];
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i = 0, n = strlen(key); i < n; i++)
    {
        if (!isdigit(key[i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    int koker = atoi(key);
    string s = get_string("plaintext: ");

    printf("ciphertext: ");

    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if(isalpha(s[i]))
        {
            if(isupper(s[i]))
            {
                printf("%c", (s[i] - 65 + koker) % 26 + 65);
            }
            if(islower(s[i]))
            {
                printf("%c", (s[i] - 97 + koker) % 26 + 97);
            }
        }
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");





}



