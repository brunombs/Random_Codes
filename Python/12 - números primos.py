número = int(input('Digite um número: '))
número1 = int(input('Digite outro número: '))
primos = list()
for i in range(número, número1):
    if número > 1:
        for i in range(2, número):
            if número % i == 0:
                print(número, 'não é primo')
                break
        else:
            print(número, 'é primo')
            primos.append(número)
    elif número == 0:
        print(número, 'é zero')
    elif número == 1:
        print(número, 'é um')
    else:
        print(número, 'é negativo')
    número+= 1
print(f'A lista com os números primos é: {primos}')