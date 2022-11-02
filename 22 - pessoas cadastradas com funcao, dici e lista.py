dici = dict()
lista = list()
def pessoa():
    dici['nome'] = str(input('Digite o nome da pessoa: '))
    print(dici["nome"])


def idade():
    dici['idade'] = int(input('Digite a idade dessa pessoa: '))
    print(dici["idade"])


while True:
    pessoa()
    idade()
    quercontinuar = str(input('Deseja continuar? [S/N]: ')).upper()
    lista.append(dici.copy())
    if quercontinuar == 'N':
        break
for indice, valor in enumerate(lista):
    print(f'A pessoa com registro {indice}, tem nome: {lista[indice]["nome"]} e idade {lista[indice]["idade"]}')