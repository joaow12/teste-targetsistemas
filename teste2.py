#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
# pertence ou não a sequência.

num1 = 0
num2 = 0
z = 3 #O número que deseja saber se pertence a sequencia
aparece = False

while(num2<3000):
    num2 = num2+num1
    num1 = num2-num1

    if num2 == 0:
        num2 = num2+1

    if z == num2 or z == num1:
        aparece = True

if aparece == True:
    print('O número digitado ({0}) aparece na sequencia'.format(z))
else:
    print('O número digitado ({0}) não aparece na sequencia'.format(z))