from random import randint
rolarodado = (input('Você quer rolar o dado? [S/N]: ')).upper()
while rolarodado != ('S') and rolarodado != ('N'):
    rolarodado = str(input('Opção inválida, tente novamente! Use "S" para sim e "N" para não!: ')).upper()
if rolarodado == ('N'):
    print('Quem sabe numa próxima vez :)')
elif rolarodado == ('S'):
    valor1 = int(input('Digite o valor inicial do dado: '))
    valor2 = int(input('Digite o valor final do dado: '))
while rolarodado == ('S'):
    print(randint(valor1, valor2))
    rolarodado = str(input('Você quer rolar o dado novamente? [S/N]: ')).upper()
    while rolarodado != ('S') and rolarodado != ('N'):
        rolarodado = str(input('Opção inválida, tente novamente! Use "S" para sim e "N" para não!: ')).upper()
    if rolarodado == ('N'):
        break
print('Obrigado por ter jogado, até a próxima!')