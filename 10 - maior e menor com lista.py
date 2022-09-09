lista = list()
maior = 0
menor = 0
for cont in range (0, 5):
    lista.append(int(input(f'Digite um número para a posição {cont}: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print('='*90)
print(f'Você digitou os valores {lista}')
print(f'Os valores digitados em ordem crescente são: {sorted(lista)}')
print('='*90)
print(f'O maior valor digitado foi: {maior} e ele se encontra nas posições: ', end='')
for cont, número in enumerate(lista):
    if maior == número:
        print(f'{cont}... ', end='')
print()
print(f'O menor valor digitado foi: {menor} e ele se encontra nas posições: ', end='')
for cont, número in enumerate(lista):
    if menor == número:
        print(f'{cont}... ', end='')
print()
print('='*90)