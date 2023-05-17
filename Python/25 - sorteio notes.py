from time import sleep
import random
lista = []
macbook = {
  "marca": "apple",
  "processador": "core2duo",
  "memória ram": "6gb ddr3",
  "tamanho da tela": "13.3",
  "gpu": "nvidia geforce 320m",
  "ano do modelo": "2010"
}
alienware = {
  "marca": "dell",
  "processador": "ryzen",
  "memória ram": "16gb ddr4",
  "tamanho da tela": "15.6",
  "gpu": "rtx 3080",
  "ano do modelo": "2022"
}
lenovo = {
  "marca": "lenovo",
  "processador": "intel",
  "memória ram": "4gb ddr4",
  "tamanho da tela": "14",
  "gpu": "uhd 530",
  "ano do modelo": "2016"
}
lista.append(macbook)
lista.append(alienware)
lista.append(lenovo)
print('Temos laptops das marcas: ')
for item in lista:
  print(item["marca"].upper())
  sleep(0.3)
while True:
  querparticipar = input('Você quer participar do sorteio dos notes por apenas 1 BTC? Responda [S] ou [N]: ').upper()
  if querparticipar in 'SN':
    if querparticipar == 'N':
      print('OK, quem sabe da próxima vez!')
      break
    elif querparticipar == 'S':
      print('BOA!!! VAMOS LÁ DESCOBRIR QUAL NOTE VOCÊ GANHOU!')
      cont = 5
      while cont != 0:
        print(f'{cont}...')
        cont -= 1
        sleep(1)
      notebookselecionado = random.choice(lista)
      print(f'PARABÉNS! Você ganhou um notebook da marca {notebookselecionado["marca"]}')
      print(f'''As confs dele são:
Processador: {notebookselecionado["processador"]}
Memória RAM: {notebookselecionado["memória ram"]}
Tamanho da tela: {notebookselecionado["tamanho da tela"]}
GPU: {notebookselecionado["gpu"]}
Ano do modelo: {notebookselecionado["ano do modelo"]} 
''')
      satisfeito = input('Está satisfeito com o resultado? Caso não esteja, tem uma chance para trocar, basta digitar "N", do contrário, digite "S" para encerrar: ').upper()
      if satisfeito in 'SN':
        if satisfeito == 'N':
          lista.remove(notebookselecionado)
          novonote = random.choice(lista)
          print(f'OK, seu novo note é da da marca: {novonote["marca"]} !')
          print(f'''As confs dele são:
          Processador: {novonote["processador"]}
          Memória RAM: {novonote["memória ram"]}
          Tamanho da tela: {novonote["tamanho da tela"]}
          GPU: {novonote["gpu"]}
          Ano do modelo: {novonote["ano do modelo"]}
          ''')
          print('Esse é o resultado final do sorteio, aproveite seu note!!!')
          break
        elif satisfeito == 'S':
          print('AÍ SIM!!! Aproveite seu novo note!!!')
          break
