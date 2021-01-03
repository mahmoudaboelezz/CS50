#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int r = 0; r < height; r++) {
        for (int c = 0; c < width; c++) {
            RGBTRIPLE pixel = image[r][c];
            BYTE colour = (pixel.rgbtBlue + pixel.rgbtRed + pixel.rgbtGreen)/3;
            RGBTRIPLE result;
            result.rgbtGreen = colour;
            result.rgbtRed = colour;
            result.rgbtBlue = colour;
            image[r][c] = result;
            printf("%c", "H");
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
