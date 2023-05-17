lista = list()
idades = 0
while True:
    convidado = str(input('Digite o nome do convidado: '))
    idade = int(input('Digite a idade do convidado: '))
    idades += idade
    lista.append(convidado)
    lista.append(idade)
    print(lista)
    quercontinuar = str(input('Quer continuar? [S/N]: ')).upper()
    if quercontinuar == 'N':
        break
print('*-'*30)
print(f'A quantidade de convidados para o aniversário é: {(len(lista))/2}')
print('*-'*30)
print(f'A média de idade dos convidados é: {idades/(len(lista)/2)}')
print('*-'*30)
print('Os convidados são:')
for i, v in enumerate(lista):
    if i % 2 == 0:
        print(f'-> {v}'.upper())