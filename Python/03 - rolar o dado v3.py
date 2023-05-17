from random import randint
rolarodado = str(input('Você quer rolar o dado? [S/N]: ')).upper()
if rolarodado == ('N'):
    print('Até a próxima :)')
while rolarodado != ('S') and rolarodado != ('N'):
    print('Opção inválida, digite apenas "S" para sim ou "N" para não.')
    rolarodado = str(input('Você quer rolar o dado? [S/N]: ')).upper()
if rolarodado == ('S'):
    valor1 = int(input('Digite o número inicial do dado: '))
    valor2 = int(input('Digite o número final do dado: '))
while rolarodado == ('S'):
    print(randint(valor1, valor2))
    rolarodado = str(input('Você quer rolar o dado novamente? [S/N]: ')).upper()
    if rolarodado == ('N'):
        print('Obrigado por ter jogado!')
    while rolarodado != ('S') and rolarodado != ('N'):
        print('Opção inválida, digite apenas "S" para sim ou "N" para não.')
        rolarodado = str(input('Você quer rolar o dado? [S/N]: ')).upper()