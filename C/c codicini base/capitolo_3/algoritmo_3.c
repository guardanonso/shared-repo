#include <stdio.h>

int main(void){
    int test_counter = 1;
    int result = 0, passed_counter = 0, failed_counter = 0;
    
    while(test_counter <= 10){
        printf("Enter result: ");
        scanf("%d", &result);
        if (result == 1){
            passed_counter += 1;
        }
        else if (result == 2){
            failed_counter += 1;
        }
        test_counter += 1;
        printf("%d %d\n", passed_counter, failed_counter);
    }
    printf("Students who passed the exam: %d \nStudents who failed the exam: %d\n", passed_counter, failed_counter);
    if (passed_counter > 8){
        puts("Bonus to instructor!");
    }
}   