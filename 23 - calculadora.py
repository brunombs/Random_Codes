from time import sleep
def linhas():
    print('-'*45)
def soma(a, b, c):
    soma = int(a) + int(b) + int(c)
    print(f'A soma dos valores é: {soma}')

def multiplicação(a, b):
    multiplicação = int(a) * int(b)
    print(f'A multiplicação dos valores é: {multiplicação}')

def divisão(a, b):
    divisão = int(a) / int(b)
    print(f'A divisão dos valores é: {divisão}')

def subtração(a, b):
    subtração = int(a) - int(b)
    print(f'A subtração do primeiro valor pelo segundo valor é: {subtração}')

linhas()
print('Seja bem-vindo ao mundo de Python')
linhas()
sleep(3)
print('Nesse programa você terá acesso a uma calculadora virtual')
linhas()
sleep(3)
print('A primeira fase é o resultado da soma entre três valores, digite os números, um de cada vez: ')
soma(input(), input(), input())
sleep(3)
print('A segunda fase é o resultado da multiplicação entre dois valores, digite os números, um de cada vez: ')
multiplicação(input(), input())
sleep(3)
print('A terceira fase é o resultado da divisão entre dois valores, digite os números, um de cada vez: ')
divisão(input(), input())
sleep(3)
print('A quarta e última fase é o resultado da subtração entre o primeiro e o segundo valor, digite os números, um de cada vez: ')
subtração(input(), input())
linhas()
print('OBRIGADO POR UTILIZAR A CALCULADORA!')