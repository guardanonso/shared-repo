#include <stdio.h> 

/*
    commento
*/

int main(void) 
{
    /*
    Dichiarazione variabili, di diverso tipo, int e float
    */

    int height, length, width, volume;
    float profit;

    /*
    Assegno valore alle variabili
    */

    height = 8; length = 12; width = 10;
    profit = 250.75f;

    /*
    ora posso usare e variabili per calcolare cose
    */

    volume = height * length * width;
    printf("Volume: %d\n", volume);
    printf("Volume: %d\n", height * length * width); /* sono equivalenti */

    float divisione = (float)volume/11; /* devo settare la variabile*/
    printf("Divisione %f\n", divisione);

    /*
    ora posso stampare il valore di volume dopo l'operazione
    */

    printf("Height: %d\n", height);
    printf("Profit: %.10f\n", profit); /* posso mettere .n tra % e f per val stampare n cifre decimali dopo la virgola*/
    printf("Height: %d length: %d width %d\n", height, length, width); /* stampare più variabili */
    
    printf("ciau:\n");
    printf("eccetera :3\n");

    /* leggere un input dall'utente */
    int i;
    scanf("%d", &i);

    return 0;
}