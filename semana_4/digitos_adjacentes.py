"""
Exercício 2 - Desafio do vídeo "Repetição com while"
Escreva um programa que receba um número inteiro na 
entrada e verifique se o número recebido possui ao menos 
um dígito com um dígito adjacente igual a ele. 
Caso exista, imprima "sim"; se não existir, imprima "não".
"""

num = int(input("Digite um número inteiro: "))
possui_adjacente = False
aux = num
while (not possui_adjacente and aux != 0):
    digito_1 = aux % 10
    temp = aux // 10
    digito_2 = temp % 10
    aux //= 10
    if (digito_1 == digito_2):
        possui_adjacente = True

if (possui_adjacente):
    print("sim")
else:
    print("não")

