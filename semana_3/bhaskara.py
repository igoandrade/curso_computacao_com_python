"""
Exercício 2 - Desafio da videoaula
Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.

O programa deve receber os parâmetros  a a,  b b, e  c c da equação  ax^2 + bx + c ax 
2
 +bx+c, respectivamente, e imprimir o resultado na saída da seguinte maneira:

Quando não houver raízes reais imprima:

esta equação não possui raízes reais

Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade 2) imprima:

a raiz desta equação é X

ou

a raiz dupla desta equação é X

onde X é o valor da raiz dupla

Quando houver duas raízes reais imprima:

as raízes da equação são X e Y

onde X e Y são os valor das raízes.

Além disso, no caso de existirem 2 raízes reais distintas, elas devem ser impressas em ordem crescente. Exemplos:

as raízes da equação são 1.0 e 2.0

as raízes da equação são -2.0 e 0.0
"""
import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

discriminante = b**2 - 4 * a * c

if (discriminante < 0):
    print("esta equação não possui raízes reais")
elif (discriminante == 0):
    raiz_unica = -b/(2*a)
    print(f"a raiz desta equação é {raiz_unica}")
else:
    raiz1 = (-b - math.sqrt(discriminante))/(2*a)
    raiz2 = (-b + math.sqrt(discriminante))/(2*a)
    raiz1, raiz2 = min(raiz1, raiz2), max(raiz1, raiz2)
    print(f"as raízes da equação são {raiz1} e {raiz2}")
