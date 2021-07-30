"""
Exercício 1
Escreva um programa que receba um número inteiro positivo 
na entrada e verifique se é primo. Se o número for primo, 
imprima "primo". Caso contrário, imprima "não primo".
"""
import math
num = int(input("Digite um número inteiro: "))
parada = int(math.sqrt(num))+1
eh_primo = True
i = 2
while (i <= parada and eh_primo):
    if(num % i ==0):
        eh_primo = False
    i += 1

if (eh_primo):
    print("primo")
else:
    print("não primo")


