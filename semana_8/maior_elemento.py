"""
Exercício 1 - Maior elemento de uma lista
Escreva a função maior_elemento que recebe como parâmetro uma 
lista com números inteiros e devolve um número inteiro correspondente 
ao maior valor presente na lista recebida.
"""

def maior_elemento(lista):
    maior = lista[0]
    for item in lista:
        if item > maior:
            maior = item
    return maior


def main():
    lista = [2,-5,3,3,1,9,5,1,0,-10,3,10,1,0,-2]
    print(maior_elemento(lista))

if __name__=="__main__":
    main()