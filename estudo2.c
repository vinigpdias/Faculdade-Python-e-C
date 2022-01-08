#include <stdio.h>
#include <locale.h>
int main(){
    setlocale(LC_ALL, "");
    int x;
    char letra;
    printf("digite uma letra: ");
    fflush(stdin);
    letra = getchar();
    printf("digite um número inteiro: ");
    scanf("%d", &x);
    fflush(stdin);
    printf("%c", letra);
    printf("%d", x);
}