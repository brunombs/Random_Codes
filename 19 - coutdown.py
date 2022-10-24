from datetime import datetime
import pytz
IST = pytz.timezone('America/Sao_Paulo')
datetime_ist = datetime.now(IST)
ano = int(datetime_ist.strftime('%Y'))
mês = int(datetime_ist.strftime('%m'))
dia = int(datetime_ist.strftime('%d'))

print(f'Ano atual -> {ano}')
print(f'Mês atual -> {mês}')
print(f'Dia atual -> {dia}')
print('-'*30)
print('PREENCHA A DATA DO SEU COUNTDOWN APENAS COM NÚMEROS!!!')
anofinal = int(input('QUAL O ANO DA DATA FINAL? : '))
mesfinal = int(input('QUAL O MÊS DA DATA FINAL? : '))
diafinal = int(input('QUAL O DIA DA DATA FINAL? : '))
anosfaltam = anofinal - ano
mesesfaltam = mesfinal - mês
diasfaltam = diafinal - dia
print(f'Faltam {anosfaltam} anos, {mesesfaltam} meses e {diasfaltam} dias para a data final!')
print(f'Data atual: {datetime_ist}')
