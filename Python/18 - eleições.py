from random import randint
candidatos = ['22', '13', '12', '15']
eleito = (candidatos[randint(0, 3)])
print('=*'*30)
print('Os candidatos são:')
for número, candidato in enumerate(candidatos):
    if número == 0:
        print(f'Jair Messias Bolsonaro [{candidatos[número]}]')
    if número == 1:
        print(f'Luiz Inácio Lula da Silva [{candidatos[número]}]')
    if número == 2:
        print(f'Ciro Gomes [{candidatos[número]}]')
    if número == 3:
        print(f'Simone Tebet [{candidatos[número]}]')
print('=*'*30)
print('Qual o candidato você acha que irá ganhar?')
palpite = str(input('Digite apenas o número do candidato: '))
while palpite != '12' and palpite != '13' and palpite != '22' and palpite != '15':
    palpite = str(input('OPÇÃO INVÁLIDA! Digite apenas: "12", "13", "15" ou "22": '))
if palpite == eleito:
    print('Você acertou')
else:
    print(f'Você errou, quem ganhou foi o candidato com número: {eleito}!')