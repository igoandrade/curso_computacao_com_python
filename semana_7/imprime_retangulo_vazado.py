#coding: utf-8
"""
Exercício 2
Refaça o exercício 1 imprimindo os retângulos sem preenchimento, 
de forma que os caracteres que não estiverem na 
borda do retângulo sejam espaços.

Por exemplo:
    digite a largura: 10
    digite a altura: 3
    ##########
    #        #
    ##########

    digite a largura: 2
    digite a altura: 2
    ##
    ##
"""

def imprime_retangulo_vazado(largura, altura):
    lin = 1
    while lin <= altura:
        col = 1
        if lin == 1 or lin == altura:
            while col < largura:
                print("#", end="")
                col += 1
            print("#")
        else:
            while col <= largura:
                if col == 1:
                    print("#", end="")
                elif col < largura:
                    print(" ", end="")
                else:
                    print("#")
                col += 1
        lin += 1
        

def main():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))
    imprime_retangulo_vazado(largura, altura)


if __name__=="__main__":
    main()