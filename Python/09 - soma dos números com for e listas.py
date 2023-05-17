lista = list()
soma = 0
númerosdigitados = 0
for cont in range (0,3):
    lista.append(int(input('Digite um número para ser adicionado a lista: ')))
print(f'Os valores digitados foram: {lista}')
for cont, número in enumerate(lista):
    soma += número
    númerosdigitados += cont
print(f'Foram digitados {númerosdigitados} números')
print(f'A soma dos números da lista é: {soma}')