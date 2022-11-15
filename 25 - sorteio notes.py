from random import randint
def soma(a, b):
  sorteado = randint(0, 5)
  if sorteado == 5:
    soma = a - b
    print(f'O resultado é: {soma}')
  else:
    soma = a + b
    print(f'O resultado é: {soma}')



def subtração(a, b):
  sorteado = randint(0, 5)
  if sorteado == 5:
    subtração = a + b
    print(f'O resultado é: {subtração}')
  else:
    subtração = a - b
    print(f'O resultado é: {subtração}')



def multiplicação(a, b):
  sorteado = randint(0, 5)
  if sorteado == 5:
    multiplicação = a / b
    print(f'O resultado é: {multiplicação}')
  else:
    multiplicação = a * b
    print(f'O resultado é: {multiplicação}')


soma(3, 5)
subtração(3, 5)
multiplicação(3, 5)
