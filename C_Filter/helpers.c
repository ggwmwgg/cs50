#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, m = width; j < m; j++)
        {
            int kek = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.00);
            image[i][j].rgbtRed = kek;
            image[i][j].rgbtGreen = kek;
            image[i][j].rgbtBlue = kek;

        }

    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sred;
    int sgreen;
    int sblue;

    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, m = width; j < m; j++)
        {
            sred = round((0.393 * image[i][j].rgbtRed) + (0.769 * image[i][j].rgbtGreen) + (0.190 * image[i][j].rgbtBlue));
            if (sred > 255 || sred < 0)
            {
                sred = 255;
            }
            sgreen = round((0.349 * image[i][j].rgbtRed) + (0.686 * image[i][j].rgbtGreen) + (0.168 * image[i][j].rgbtBlue));
            if (sgreen > 255 || sgreen < 0)
            {
                sgreen = 255;
            }
            sblue = round((0.272 * image[i][j].rgbtRed) + (0.534 * image[i][j].rgbtGreen) + (0.131 * image[i][j].rgbtBlue));
            if (sblue > 255 || sblue < 0)
            {
                sblue = 255;
            }
            image[i][j].rgbtRed = sred;
            image[i][j].rgbtGreen = sgreen;
            image[i][j].rgbtBlue = sblue;

        }

    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, m = width / 2; j < m; j++)
        {
            RGBTRIPLE kek = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = kek;

        }

    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE kek[height][width];
    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, m = width; j < m; j++)
        {
            kek[i][j] = image[i][j];

        }

    }

    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, m = width; j < m; j++)
        {
            int totalRed, totalBlue, totalGreen;
            totalRed = totalBlue = totalGreen = 0;
            float counter = 0.00;

            //Neighbour pixels
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    int CurrentX = i + x;
                    int CurrentY = j + y;

                    //If pixel valid
                    if (CurrentX < 0 || CurrentX > (height - 1) || CurrentY < 0 || CurrentY > (width - 1))
                    {
                        continue;
                    }

                    //Img value
                    totalRed += image[CurrentX][CurrentY].rgbtRed;
                    totalBlue += image[CurrentX][CurrentY].rgbtBlue;
                    totalGreen += image[CurrentX][CurrentY].rgbtGreen;

                    counter ++;
                }

                //Avg of neighbouring pix
                kek[i][j].rgbtRed = round(totalRed / counter);
                kek[i][j].rgbtBlue = round(totalBlue / counter);
                kek[i][j].rgbtGreen = round(totalGreen / counter);
            }

        }
    }

    //Move/copy to original
    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, m = width; j < m; j++)
        {
            image[i][j].rgbtRed = kek[i][j].rgbtRed;
            image[i][j].rgbtBlue = kek[i][j].rgbtBlue;
            image[i][j].rgbtGreen = kek[i][j].rgbtGreen;
        }
    }
    return;
}
