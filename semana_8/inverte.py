"""
Exercício 2 - Invertendo sequência
Como pedido na primeira video-aula desta semana, escreva um programa que 
recebe uma sequência de números inteiros e imprima todos os valores 
em ordem inversa. A sequência sempre termina pelo número 0. 
Note que 0 (ZERO) não deve fazer parte da sequência.
"""

def inverte_lista(lista):
    lista_invertida = []
    i = len(lista)-1
    while i >= 0:
        lista_invertida.append(lista[i])
        i -= 1
    return lista_invertida

def main():
    n = 1
    i = 1
    lista = []
    while n!= 0:
        n = int(input(f"Digite o {i}º elento da lista (digite 0 para sair): "))
        if n != 0:
            lista.append(n)
        i += 1
        
    lista_invertida = inverte_lista(lista)
    for i in lista_invertida:
        print(i)


if __name__=="__main__":
    main()