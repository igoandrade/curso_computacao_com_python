"""
Exercício 1 - Par ou ímpar?
Receba um número inteiro na entrada e imprima

 par 

quando o número for par ou

ímpar

quando o número for ímpar.
"""

print("Entrada de Dados:")
numero = int(input("Digite um número inteiro: "))
print("\nSaída de Dados:")
print(f"O número {numero} é:")
if (numero % 2 == 0):
    print("par")
else:
    print("ímpar")
