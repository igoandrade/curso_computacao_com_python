"""
Exercício 2 - Primos
Escreva a função maior_primo que recebe um número inteiro 
maior ou igual a 2 como parâmetro e devolve o maior número 
primo menor ou igual ao número passado à função
"""


import math

def eh_primo(num):
    if num == 0 or num == 1:
        return False
    parada = int(math.sqrt(num))
    primalidade = True
    i = 2
    while (i <= parada and primalidade):
        if(num % i ==0):
            primalidade = False
        i += 1
    return primalidade


def maior_primo(num):
    while num >= 2:
        if eh_primo(num):
            return num
        else:
            num -= 1
