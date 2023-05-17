print('='*30)
print('QUIZ GAME')
print('='*30)
pontuação = 0

print('O sistema operacional criado por Bill Gates é o Linux! Essa afirmação é verdadeira? [S/N]')
r1 = input('RESPOSTA: ').lower()
if r1 == 'n':
    pontuação += 1
    print('Você acertou, parabéns!')
else:
    print('Infelizmente você errou! Bill Gates criou o Windows.')
print('O Linux é gratuito! Essa afirmação é verdadeira? [S/N]?')
r2 = input('RESPOSTA: ').lower()
if r2 == 's':
    pontuação += 1
    print('Você acertou, parabéns!')
else:
    print('Infelizmente você errou! O Linux é totalmente gratuito!')
print('O MacOS é o sistema operacional da Apple desenvolvido por Steve Jobs! Essa afirmação é verdadeira? [S/N]')
r3 = input('RESPOSTA: ').lower()
if r3 == 's':
    pontuação += 1
    print('Você acertou, parabéns!')
else:
    print('Infelizmente você errou! O MacOS foi desenvolvido pela Apple com Steve Jobs!')
print('É possível adicionar cores nas palavras em Python. Essa afirmação é verdadeira? [S/N]')
r4 = input('RESPOSTA: ').lower()
if r4 == 's':
    pontuação += 1
    print('Você acertou, parabéns!')
else:
    print('Infelizmente você errou! É possível adicionar cores nas palavras em Python.')
print('Esse quiz é ruim! Essa afirmação é verdadeira? [S/N]')
r5 = input('RESPOSTA: ').lower()
if r5 == 'n':
    pontuação += 1
    print('Parabéns, você acertou!!! Essa foi fácil :D')
else:
    print('Infelizmente você ERROU FEIO! Esse quiz é EXCELENTE!')
print(f'Sua pontuação final foi: {pontuação}/5')
