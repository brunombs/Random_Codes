empresas = ('warmup', 'techno', 'tetris', 'golden', 'raio', 'lantech', 'techforgaming', 'orange')
print('A palavra em destaque contém dentro dela a palavra "tech"?')
print('='*50)
for cont in empresas:
    print(f'\nPalavra: {cont.upper()} ', end='')
    if 'tech' in cont:
        print('contém a palavra tech', end=' ')
    else:
        print('não contém a palavra tech', end='')
print('\n')
print('='*50)