"""
Exercício 1 - Removendo elementos repetidos
Escreva a função remove_repetidos que recebe como parâmetro uma lista 
com números inteiros, verifica se tal lista possui elementos repetidos 
e os remove. A função deve devolver uma lista correspondente à primeira 
lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
"""

def remove_repetidos(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    nova_lista.sort()
    return nova_lista

def main():
    lista = [2,-5,3,3,1,9,5,1,0,-10,3,10,1,0,-2]
    print(remove_repetidos(lista))

if __name__=="__main__":
    main()