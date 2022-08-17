from random import randint
rolarodado = str(input('Você quer rolar o dado? [S/N] ')).upper()
while rolarodado != ('S') and rolarodado != ('N'):
    print('Opção inválida, tente "S" para rolar o dado ou "N" para encerrar.')
    rolarodado = str(input('Você quer rolar o dado? [S/N] ')).upper()
if rolarodado == ('S'):
    dado = randint(1, 6)
    print('O resultado foi: {} '.format(dado))
elif rolarodado == ('N'):
    print('Até a próxima :D')