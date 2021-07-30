"""
Exercício 2
Receba um número inteiro positivo na entrada e imprima os 
n primeiros números ímpares naturais. 
Para a saída, siga o formato do exemplo abaixo.
"""

num = int(input("Digite o valor de n: "))
i = 1
while (i <= num):
    print(2*i - 1)
    i += 1
