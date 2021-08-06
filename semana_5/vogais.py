"""
Exercício 3 - Vogais
Escreva a função vogal que recebe um único caractere 
como parâmetro e devolve True se ele for uma vogal e False 
se for uma consoante.
"""

def vogal(caractere):
    lista_vogais = ["a", "e", "i", "o", "u"]
    caractere = caractere.lower()
    if caractere in lista_vogais:
        return True
    else:
        return False

teste = "OsvaloresTrueeFalsedevolvidosdevemserdotipoboolbooleanosenaostrings"
for t in teste:
    print(t, vogal(t))