#include <stdio.h>

int main(void) {
    int counter, c, grades_sum, class_avg;
    counter = 1;
    grades_sum = 0;

    while(counter <= 10){
        printf("Enter a grade: ");
        scanf("%d", &c);
        grades_sum += c;
        counter += 1;
    }
    class_avg = grades_sum/10;
    printf("Avarage grade of the class is: %d", class_avg);


}