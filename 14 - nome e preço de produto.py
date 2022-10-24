produtoepreço = list()
valores = list()
somadospreços = 0
while True:
    valores.append(str(input('Digite o nome do produto: ')))
    valores.append(int(input('Digite o preço do produto: ')))
    somadospreços += valores[1]
    produtoepreço.append(valores[:])
    quercontinuar = (str(input('Você deseja continuar? [S/N]: '))).upper()
    if quercontinuar == 'N':
        break
    valores.clear()
print(produtoepreço)
print('A lista com os produtos é: ')
for cont, valor in enumerate(produtoepreço):
    print(valor[0])
print(f'A soma dos preços é: {somadospreços} R$')
