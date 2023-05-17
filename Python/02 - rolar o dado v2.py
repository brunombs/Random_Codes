from random import randint
querrolar = str(input('Você quer rolar o dado? [S/N]: ')).upper()
if querrolar == ('N'):
    print('Obrigado, até a próxima :)')
while querrolar == ('S'):
    print(randint(1, 6))
    querrolar = str(input('Você quer rolar o dado novamente? [S/N]: ')).upper()
    if querrolar != ('S') and querrolar != ('N'):
        print('Opção inválida, tente novamente digitando "S" para sim e "N" para não.')
        querrolar = str(input('Você quer rolar o dado? [S/N]: ')).upper()
    elif querrolar == ('N'):
        print('Obrigado por jogar, até a próxima vez!')