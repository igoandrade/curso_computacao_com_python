#coding: utf-8
"""
Exercício 2 - (Difícil) Soma das hipotenusas
Dizemos que um número é uma hipotenusa de um triângulo inteiro se existe 
um triângulo retângulo com lados inteiros cuja hipotenusa é igual a esse número. 
Em outras palavras, nn é uma hipotenusa se existem números inteiros ii e jj tais que:

    n**2 = i**2 + j**2

Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo n
e devolva a soma de todos os inteiros entre 1 e n que são comprimento da hipotenusa de 
algum triângulo retângulo com catetos inteiros.

Dica1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser somado apenas uma vez. 
Uma boa solução para este exercício é fazer um laço de 1 até n testando se o número é hipotenusa 
de algum triângulo e somando em caso afirmativo. Uma solução que dificilmente vai dar 
certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.

Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o comprimento da 
hipotenusa de um triângulo com lados de comprimento inteiro ou não.
"""

def é_hipotenusa(n):
    for i in range(1, n):
        for j in range(n-1, 0, -1):
            if (n**2 == i**2 + j**2):
                return True
    return False

def soma_hipotenusas(n):
    soma = 0
    for i in range(2, n+1):
        if é_hipotenusa(i):
            soma += i
    return soma
