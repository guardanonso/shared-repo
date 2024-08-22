#include <stdio.h>

int main(void) {
    int c = getchar();

    int truth = c != EOF;
    printf("%d\n", truth);

    printf("Il valore di EOF è: %d\n", EOF);  // Assicurati che il file sia salvato in UTF-8
    return 0;
}