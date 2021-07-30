"""
Exercício 2
Faça um programa em Python que receba quatro notas, calcule e imprima a 
média aritmética. Observe o exemplo abaixo:

Exemplo:

Entrada de Dados:
Digite a primeira nota: 4

Digite a segunda nota: 5

Digite a terceira nota: 6

Digite a quarta nota: 7

Saída de Dados:
A média aritmética é 5.5
"""

lista_notas = ['primeira', 'segunda', 'terceira', 'quarta']
notas = []
print("Entrada de Dados:")
for i in lista_notas:
    nota = float(input(f"Digite a {i} nota: "))
    notas.append(nota)

print("\nSaída de Dados:")
nota_media = sum(notas)/len(notas)
print(f"A média aritmética é {nota_media}")