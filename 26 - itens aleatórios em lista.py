import numpy.random as random
from time import sleep
def pessoas():
  lista = ['bruno', 'gabriel', 'gleide', 'valter', 'druid', 'nino']
  sorteado = (random.choice(lista))
  if sorteado == 'bruno':
    print(f'O mais lindo da casa é: {sorteado}')
  elif sorteado == 'gabriel':
    print(f'O mais feio da casa é: {sorteado}')
  elif sorteado == 'gleide':
    print(f'A melhor pessoa da casa é {sorteado}')
  elif sorteado == 'valter':
    print(f'O melhor homem da casa é: {sorteado}')
  elif sorteado == 'druid':
    print(f'O cachorro mais teimoso é: {sorteado}')
  elif sorteado == 'nino':
    print(f'O cachorro mais atrapalhado é: {sorteado}')


lista2 = []
while True:
  pessoas()
  add = (input('Adicione itens aleatórios a uma lista e receba uma mensagem: '))
  lista2.append(add)
  print(lista2)
  querdnv = input('Quer adicionar outro item? Digite [N] caso não queira: ').upper()
  print('Obrigado por participar!')
  if querdnv == 'N':
    break

print('Os itens que foram listados são: ')
for item in lista2:
  print(item)
  sleep(0.5)
print(f'Foram listados {len(lista2)} itens!')
print('Fim do programa!')