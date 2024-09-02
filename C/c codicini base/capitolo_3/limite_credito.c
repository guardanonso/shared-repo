#include <stdio.h>

int main(void){
    
    int account_number;
    float credit_limit, beginning_balance, total_charges, total_credits;

    float balance;


    while(1){
        printf("Enter account number (-1 to end): ");
        scanf("%d", &account_number);
        if(account_number == -1){
            break;
        }

        printf("Enter beginning balance: ");
        scanf("%f", &beginning_balance);

        printf("Enter total charges: ");
        scanf("%f", &total_charges);

        printf("Enter total credits: ");
        scanf("%f", &total_credits);

        printf("Enter credit limit: ");
        scanf("%f", &credit_limit);

        balance = beginning_balance + total_charges - total_credits;

        if(balance > credit_limit){

            printf("Account: %d\n", account_number);
            printf("Credit limit: %f\n", credit_limit);
            printf("Balance: %f\n", balance);

            puts("Credit Limit Exceeded."); 
        }
        printf("ciaooo");
    }
}