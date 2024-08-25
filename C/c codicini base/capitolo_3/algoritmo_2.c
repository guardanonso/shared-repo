#include <stdio.h>

int main(void){
    int total;
    int counter = 0;
    int grade;

    printf("Enter a grade: ");
    scanf("%d", &grade);
    while(grade != -1){
        counter += 1;
        total += grade;
        printf("Enter a grade: ");
        scanf("%d", &grade);
    }
    if (total != 0){
        float result = (float) total / counter;
        total / counter;
        printf("Avarage grade is: %.2f", result);
    }
    else {
        puts("No grades were entered");
    }
}