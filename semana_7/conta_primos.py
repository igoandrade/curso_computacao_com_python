#coding: utf-8

"""
Exercício 1 - Primos
Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual 
a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n 
(incluindo 2 e, se for o caso, n).

Exemplo:

    >>>n_primos(2)
    1
    >>>n_primos(4)
    2
    >>>n_primos(121)
    30
"""

import math

def eh_primo(num):
    n_parada = int((math.sqrt(num)))
    for i in range(2, n_parada+1):
        if num % i == 0:
            return False
    return True

def n_primos(num):
    qnt_primos = 0
    for i in range(2, num+1):
        if eh_primo(i):
            qnt_primos += 1
    return qnt_primos


def main():
    for i in [2, 4, 19, 20, 47, 113, 121, 1000, 10000]:
        print(f"{i} --> {n_primos(i)}")

if __name__=="__main__":
    main()