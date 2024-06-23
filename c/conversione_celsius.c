#include <stdio.h>

int main() 
{
    float fahr = 0, celsius; 
    int upper, lower, step;

    step = 20; 
    upper = 300;

    while (fahr <= upper) {
        celsius = (5.0/9.0) * (fahr-32);
        printf("Fahr: %3.0f\t Celsius: %5.1f\n", fahr, celsius);
        fahr = fahr + step; 
    }
}