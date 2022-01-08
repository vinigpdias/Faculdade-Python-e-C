#include <stdio.h>
#include <locale.h>
int main() {
    setlocale (LC_ALL, "");
    int idade;
    char eCivil;
    printf("Vocé pode digitar sua idade? ");
    scanf("%d", &idade);
    printf("%d anos", idade);
    printf("\nDigite C para casado ou S para solteiro");
    fflush (stdin);
    eCivil = getchar ();
    printf("Você digitou %c", eCivil);
}