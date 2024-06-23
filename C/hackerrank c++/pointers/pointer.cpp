#include <stdio.h>

void update(int *a, int *b) {
    int first = *a;
    int second = *b;
    if(first>=second){
        *a = first + second;
        *b = first - second;
    }
    else{
        *a = first + second;
        *b = (first - second) * -1;
    }
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
