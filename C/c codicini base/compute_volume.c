#include <stdio.h>
int main(void)
{
    int height, length, width;
    printf("Enter height of the box:\n");
    scanf("%d", &height);
    printf("Enter the length:\n");
    scanf("%d", &length);
    printf("Enter the width:\n");
    scanf("%d", &width);

    printf("Volume: %d", height*length*width);
    return 0;
}