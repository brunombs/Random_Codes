print('='*30)
print('QUIZ GAME')
print('='*30)
pontuação = 0

print('Qual é a forma correta para exibir texto em Python?\n'
      '[1] printf(Python")\n'
      '[2] print"Python")\n'
      '[3] print("Python")\n'
      '[4] print(fPython)')
r1 = input('RESPOSTA: ')
if r1 == '3':
    pontuação += 1
    print('Parabéns, você acertou!')
else:
    print('Infelizmente você errou.')
print('Qual é a forma correta para obter um dado do usuário em Python?\n'
      '[1] input("Dado do usuário aqui")\n'
      '[2] print("Dado do usuário aqui")\n'
      '[3] dataget("Dado do usuário aqui")\n'
      '[4] dataf("Dado do usuário aqui")')
r2 = input('RESPOSTA: ')
if r2 == '1':
    pontuação += 1
    print('Parabéns, você acertou!')
else:
    print('Infelizmente você errou.')
print('Qual método em strings que faz todas as palavras ficarem minúsculas?\n'
      '[1] .upper()\n'
      '[2] .min()\n'
      '[3] .lower()\n'
      '[4] .small()')
r3 = input('RESPOSTA: ')
if r3 == '3':
    pontuação += 1
    print('Parabéns, você acertou!')
else:
    print('Infelizmente você errou.')
print('Qual é o operador lógico para verificar se dois valores são distintos?\n'
      '[1] ==\n'
      '[2] <>\n'
      '[3] ><\n'
      '[4] !=')
r4 = input('RESPOSTA: ')
if r4 == '4':
    pontuação += 1
    print('Parabéns, você acertou!')
else:
    print('Infelizmente você errou.')
print('Tuplas são mutáveis. Essa afirmação é verdadeira?\n'
      '[1] Verdadeiro\n'
      '[2] Falso')
r5 = input('RESPOSTA: ')
if r5 == '2':
    pontuação += 1
    print('Parabéns, você acertou!')
else:
    print('Infelizmente você errou.')
print(f'A sua pontuação foi: {pontuação}/5')