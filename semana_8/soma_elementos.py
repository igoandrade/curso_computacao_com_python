"""
Exercício 2 - Soma dos elementos de uma lista
Escreva a função soma_elementos que recebe como parâmetro uma 
lista com números inteiros e devolve um número inteiro correspondente 
à soma dos elementos da lista recebida.
"""

def soma_elementos(lista):
    return sum(lista)

def main():
    lista = [2,-5,3,3,1]
    print(soma_elementos(lista))

if __name__=="__main__":
    main()