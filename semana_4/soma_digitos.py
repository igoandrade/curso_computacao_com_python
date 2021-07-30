"""
Exercício 3
  Escreva um programa que receba um número inteiro na entrada, 
  calcule e imprima a soma dos dígitos deste número na saída
"""


num = int(input("Digie um número inteiro: "))
aux = num
soma = 0

while aux != 0:
    
    digito = aux % 10
    aux //=  10
    soma += digito


print(soma)