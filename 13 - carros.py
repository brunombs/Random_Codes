carros = list()
nomeemarca = list()
totaldecarros = 0
while True:
    nomeemarca.append(str(input('Digite o nome de um veículo: ')))
    totaldecarros += 1
    if carros in carros:
        print('Esse modelo já foi registrado no nosso banco de dados.')
    nomeemarca.append(str(input('Digite a marca do veículo: ')))
    print(carros)
    print(nomeemarca)
    carros.append(nomeemarca[:])
    queradicionar = str(input('Você deseja continuar? [S/N]: ')).upper()
    if queradicionar != 'N' and queradicionar != 'S':
        queradicionar = str(input('OPÇÃO INVÁLIDA! Digite "S" para continuar ou "N" para encerrar: ')).upper()
    if queradicionar == 'N':
        break
    print(nomeemarca)
    nomeemarca.clear()
    print(f'apaguei nome e marca {nomeemarca}')
print(f'O total de carros adicionados foram: {totaldecarros}')
for índice, valor in enumerate(carros):
    print(f'O {índice+1}º carro da lista é: {valor[0]} da marca {valor[1]}')