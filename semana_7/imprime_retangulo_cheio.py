#coding: utf-8
"""
Exercício 1
Escreva um programa que recebe como entradas (utilize a função input) 
dois números inteiros correspondentes à largura e à altura de um retângulo, 
respectivamente. O programa deve imprimir, usando repetições encaixadas 
(laços aninhados), uma cadeia de caracteres que represente o retângulo 
informado com caracteres '#' na saída.

Por exemplo:
    digite a largura: 10
    digite a altura: 3
    ##########
    ##########
    ##########
"""

def imprime_retangulo_cheio(largura, altura):
    for lin in range(altura):
        for col in range(largura):
            if col < largura -1:
                print("#", end="")
            else:
                print("#")
        

def main():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))
    imprime_retangulo_cheio(largura, altura)


if __name__=="__main__":
    main()