#include <stdio.h>
#include <unistd.h>

int main(void){
    int c = getchar();
    
    while(c != EOF){
        putchar(c);
        sleep(1);
        c = getchar();
    }

    return(0);
}
    
