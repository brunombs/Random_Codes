from random import randint
times = ['Corinthians', 'Flamengo']
acertos = 0
cor = 0
fla = 0
palpites = 0
while True:
    palpite = ''
    sorteio = randint(0, 1)
    ganhador = times[sorteio]
    while palpite != 'CORINTHIANS' and palpite != 'FLAMENGO':
        palpite = str(input('Quem você acha que irá vencer? Digite "Corinthians" ou "Flamengo": ')).upper()
        if palpite == ganhador.upper():
            acertos += 1
    palpites += 1
    if ganhador == 'Corinthians':
        print('Corinthians venceu')
        print('Flamengo perdeu')
        cor += 1
    elif ganhador == 'Flamengo':
        print('Flamengo venceu')
        print('Corinthians perdeu')
        fla += 1
    denovo = str(input('Você quer repetir o processo? [S/N]: ')).upper()
    if 'N' in denovo:
        print(f'Corinthians com {cor} pontos')
        print(f'Flamengo com {fla} pontos')
        print(f'Você palpitou {palpites} vezes e acertou {acertos} palpites!')
        print('Obrigado por participar!')
        break
