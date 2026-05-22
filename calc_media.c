#include <stdio.h>

float calcular_media(int numeros[], int tamanho) {
    int soma = 0;
    for(int i = 0; i < tamanho; i++) {
        soma += numeros[i];
    }
    return soma / (float)tamanho; // O (float) aqui garante a divisão decimal correta
}

int main() {
    int numeros[] = {10, 20, 30, 40, 50};
    int tamanho = sizeof(numeros) / sizeof(numeros[0]);
    
    float media = calcular_media(numeros, tamanho);
    printf("A média é: %.2f\n", media);
    
    return 0;
}
