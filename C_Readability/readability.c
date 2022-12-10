#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <stdio.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    float l = 100.00 * (float) letters / (float) words;
    float s = 100.00 * (float) sentences / (float) words;
    float index = (0.0588 * l) - (0.296 * s) - 15.8;
    int keker = round(index);
    if (keker >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (keker < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", keker);
    }

    //printf("Length: %i\nWords: %i\nSentences: %i\n", letters, words, sentences);
    //index = 0.0588 * L - 0.296 * S - 15.8
    //where L is the average number of letters per 100 words in the text,
    //and S is the average number of sentences per 100 words in the text.
}

int count_letters(string text)
{
    int kok = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            kok++;
        }
    }
    return kok;
}

int count_words(string text)
{
    int kok = 1;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == ' ' && text[i+1] != ' ')
        {
            kok++;
        }
    }
    return kok;
}

int count_sentences(string text)
{
    int kok = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            kok++;
        }
    }
    return kok;
}