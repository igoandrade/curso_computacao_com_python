"""
Exercício 1 - FizzBuzz
Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

'Fizz' se o número for divisível por 3 e não for divisível por 5;

'Buzz' se o número for divisível por 5 e não for divisível por 3;

'FizzBuzz' se o número for divisível por 3 e por 5;

Caso o número não seja divisível 3 e também não seja divisível por 5, 
ela deve devolver o número recebido como parâmetro.
"""

def fizzbuzz(num):
    if not(num % 3 == 0) and not(num % 5 == 0):
        return num
    else:
        resposta = ""
        if num % 3 == 0:
            resposta += "Fizz"
        if num % 5 == 0:
            resposta += "Buzz"
        return resposta

for i in range(103):
    print(i, fizzbuzz(i))