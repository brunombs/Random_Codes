from random import randint
list = ['1', '2', '3', '4']
def soma(a, b):
    soma = a + b
    print(f'O resultado da soma é: {soma}')



def subtração(a, b):
    subtração = a - b
    print(f'O resultado da subtração é: {subtração}')


def multiplicação(a, b):
    multiplicação = a * b
    print(f'O resultado da multiplicação é: {multiplicação}')


def divisão(a, b):
  divisão = a / b
  print(f'O resultado da divisão é: {divisão:.3f}')



while True:
  operação = str(input('''
Qual a operação matemática você deseja fazer?
[1] = SOMA
[2] = SUBTRAÇÃO
[3] = MULTIPLICAÇÃO
[4] = DIVISÃO
DIGITE AQUI O NÚMERO > '''))
  while operação not in list:
      operação = str(input('''
Digite apenas 1, 2, 3 ou 4, sendo:
1 para SOMA
2 para SUBTRAÇÃO
3 para MULTIPLICAÇÃO
4 para DIVISÃO
-> '''))
  if operação == '1':
    n1 = int(input('Digite o primeiro valor para os cálculos: '))
    n2 = int(input('Digite o segundo valor para os cálculos: '))
    soma(n1, n2)
    break
  if operação == '2':
    n1 = int(input('Digite o primeiro valor para os cálculos: '))
    n2 = int(input('Digite o segundo valor para os cálculos: '))
    subtração(n1, n2)
    break
  if operação == '3':
    n1 = int(input('Digite o primeiro valor para os cálculos: '))
    n2 = int(input('Digite o segundo valor para os cálculos: '))
    multiplicação(n1, n2)
    break
  if operação == '4':
    n1 = int(input('Digite o primeiro valor para os cálculos: '))
    n2 = int(input('Digite o segundo valor para os cálculos: '))
    divisão(n1, n2)
    break





