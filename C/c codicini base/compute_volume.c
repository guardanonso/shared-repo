#include <stdio.h>
int main(void)
{
    int height, weight, width;
    printf("Enter height of the box:\n");
    scanf("%d", &height);
    printf("Enter the weight:\n");
    scanf("%d", &weight);
    printf("Enter the width:\n");
    scanf("%d", &width);

    printf("Volume: %d", height*weight*width);
    return 0;
}