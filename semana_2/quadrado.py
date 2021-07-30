"""
Exercício 1
Faça um programa em Python que receba (entrada de dados) o valor 
correspondente ao lado de um quadrado, calcule e imprima (saída de dados) 
seu perímetro e sua área.

Observação: a saída deve estar no formato: "perímetro: x - área: y"
"""
print("Entrada de Dados:")
lado = int(input("Digite o valor correspondente ao lado de um quadrado: "))

perimetro = 4*lado
area = lado**2

print("\nSaída de Dados:")
print(f"perímetro: {perimetro} - área: {area}")