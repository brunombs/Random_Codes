valordagasolina = float(input('Digite o valor do litro da gasolina: '))
valordodiesel = float(input('Digite o valor do litro do diesel: '))
carrokm = float(input('Digite quantos KM/l o carro faz por litro: '))
motokm = float(input('Digite quantos KM/l a moto faz por litro: '))
quantoskms = int(input('Digite quantos KMs você percorre por dia: '))
quantosdias = int(input('Digite quantos dias você usará o veículo: '))
totalgastonocarro = (quantoskms / carrokm) * valordodiesel * quantosdias
totalgastonamoto = (quantoskms / motokm) * valordagasolina * quantosdias
diferença = totalgastonocarro - totalgastonamoto
totalpercorrido = quantoskms * quantosdias
print('No período de {} dias, a moto tendo percorrido o total de {} kms, gastará de combustível {:.2f} reais'.format(quantosdias, quantoskms, totalgastonamoto))
print('No período de {} dias, o carro tendo percorrido o total de {} kms, gastará de combustível {} reais'.format(quantosdias, quantoskms, totalgastonocarro))
print('A diferença entre os gastos é de {} reais'.format(diferença))
print('No período de {} dias você percorrerá {} kms'.format(quantosdias, totalpercorrido))