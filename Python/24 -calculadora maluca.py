from time import sleep
from random import randint
sorteio = randint(0, 5)
def linha():
    print('-'* 50)


def multiplicação(a, b):
    if sorteio == 5:
        multiplicação = a / b
        print('\033[31mErhh...\033[m ', end='')
    else:
        multiplicação = a * b
    print(f'O valor da multiplicação entre {a} e {b} é: {multiplicação}')


def divisão(a, b):
    if sorteio == 5:
        divisão = a * b
        print('\033[31mErhh...\033[m ', end='')
    else:
        divisão = a / b
    print(f'O valor da divisão entre {a} e {b} é: {divisão}')


def soma(a, b):
    if sorteio == 5:
        soma = a - b
        print('\033[31mErhh...\033[m ', end='')
    else:
        soma = a + b
    print(f'O valor da soma entre {a} e {b} é: {soma}')


def subtração(a, b):
    if sorteio == 5:
        subtração = a + b
        print('\033[31mErhh...\033[m ', end='')
    else:
        subtração = a - b
    print(f'O valor da subtração entre {a} e {b} é: {subtração}')

print(sorteio)
linha()
print(' '* 7 + 'SEJA BEM-VINDO A CALCULADORA MALUCA')
linha()
sleep(0.5)
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
linha()
print(' '* 7 + 'OBRIGADO POR INSERIR OS VALORES!')
linha()
sleep(1)
print('A CALCULADORA MALUCA IRÁ EXIBIR O RESULTADO DAS CONTAS BÁSICAS DESSES VALORES')
sleep(2)
print('EXISTE 20% DE CHANCE DO RESULTADO SER INVERTIDO!')
sleep(2)
multiplicação(valor1, valor2)
sleep(1)
divisão(valor1, valor2)
sleep(1)
soma(valor1, valor2)
sleep(1)
subtração(valor1, valor2)
sleep(1)