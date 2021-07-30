"""
Exercício 1
Escreva um programa que receba um número natural  n na entrada e imprima  n! fatorial) na saída.
"""

def meu_fatorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*meu_fatorial(n-1)

num = int(input("Digite o valor de n: "))
fat = meu_fatorial(num)
print(fat)