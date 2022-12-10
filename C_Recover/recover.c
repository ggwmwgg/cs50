#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;


int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        //Correct args
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    //Read
    FILE *kek = fopen(argv[1], "r");

    //Validate
    if (kek == NULL)
    {
        printf("Couldn't open file");
        return 2;
    }

    //Variables
    int counter = 0;
    unsigned char buff[512];
    FILE *outkek = NULL;
    char *filename  = malloc(8 * sizeof(char));

    //Blocks reading
    while (fread(buff, sizeof(char), 512, kek))
    {
        if (buff[0] == 0xff && buff[1] == 0xd8 && buff[2] == 0xff
        && (buff[3] & 0xf0) == 0xe0)
        {
            //1 JPEG Name/2 Open/ 3 Count
            sprintf(filename, "%03i.jpg", counter);
            outkek = fopen(filename, "w");
            counter++;
        }
        // Validity if OK
        if (outkek != NULL)
        {
            fwrite(buff, sizeof(char), 512, outkek);
        }
    }
    free(filename);
    fclose(outkek);
    fclose(kek);

    return 0;
}