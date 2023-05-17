palavras = ('word', 'office', 'excel', 'docs', 'powerpoint')
verificar = input('Digite quais letras você deseja verificar se contém nas palavras armazenadas: ')
for cont in palavras:
    print(f'A palavra {cont.upper()} ', end='')
    if verificar in cont:
        print(f'\033[1;32mcontém\033[m a(s) letra(s) {verificar}')
    else:
        print(f'\033[1;31mnão contém\033[m a(s) letra(s) {verificar}')