"""
Exercício 2 - Máximo com 3 parâmetros
Reescreva a função 'maximo' do outro exercício, 
que devolve o maior valor dentre dois inteiros recebidos, 
para que ela passe a receber 3 valores inteiros como parâmetros 
e devolva o maior dentre eles.
"""

def maximo(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= z:
        return y
    else:
        return z

