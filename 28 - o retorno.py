from time import sleep
salario_hora_hotel = 11.80
salario_hora_ondway = 13
linha = '-'*50
opcao = 0
continuar = 0
print(linha)
print('CÁLCULO DE SALÁRIO'.center(50))
print(linha)
sleep(0.5)
horas_trabalhadas_hotel = float(input('Digite a quantidade de horas que trabalhou no hotel na semana: '.center(50)))
sleep(0.1)
horas_trabalhadas_ondway = float(input('Digite a quantidade de horas que trabalhou no delivery na semana: '.center(50)))
sleep(0.1)
salario_semana = ((salario_hora_hotel * horas_trabalhadas_hotel) + (salario_hora_ondway * horas_trabalhadas_ondway))
salario_semana_descontado_imposto = (salario_hora_hotel * horas_trabalhadas_hotel * 0.80) + (salario_hora_ondway * horas_trabalhadas_ondway)
imposto = salario_hora_hotel * horas_trabalhadas_hotel * 0.20

while continuar != 2:
    print('''
O que você deseja verificar?
Digite [1] para verificar o relatório geral.
Digite [2] para verificar o relatório mensal.
Digite [3] para verificar o relatório semanal.
Digite [4] para encerrar o programa.
    ''')
    opcao = int(input('Digite o número da opção que deseja verificar: '))
    if opcao == 1:
        print(linha)
        print('MENSAL'.center(50))
        print(linha)
        print(f'O seu salário no mês: {salario_semana * 4}€')
        print(f'O seu salário no mês, descontando os impostos: {salario_semana_descontado_imposto * 4}€')
        print(f'O imposto pago no mês: {imposto * 4:.2f}€')
        print(linha)
        print('SEMANAL'.center(50))
        print(linha)
        print(f'O seu salário na semana: {salario_semana}€')
        print(f'O seu salário na semana, descontando os impostos: {salario_semana_descontado_imposto}€')
        print(f'O imposto pago na semana: {imposto:.2f}€')
        print(linha)

    elif opcao == 2:
        print(linha)
        print('MENSAL'.center(50))
        print(linha)
        print(f'O seu salário no mês: {salario_semana * 4}€')
        print(f'O seu salário no mês, descontando os impostos: {salario_semana_descontado_imposto*4}€')
        print(f'O imposto pago no mês: {imposto * 4:.2f}€')
        print(linha)

    elif opcao == 3:
        print(linha)
        print('SEMANAL'.center(50))
        print(linha)
        print(f'O seu salário na semana: {salario_semana}€')
        print(f'O seu salário na semana, descontando os impostos: {salario_semana_descontado_imposto}€')
        print(f'O imposto pago na semana: {imposto:.2f}€')
        print(linha)

    elif opcao == 4:
        continuar = 2

    if continuar == 2:
        break
    continuar = int(input('''
Deseja voltar ao menu?
Digite [1] para continuar navegando.
Digite [2] para encerrar
'''))

print('Obrigado por utilizar o nosso programa, volte sempre. :)')

