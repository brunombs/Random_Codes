import telebot
import requests
import emoji
from time import sleep
telegram_destino = '-000000000' #coloque o ID do telegram no lugar dos zeros.
CHAVE_API = "0000000000:AAAaaa-aAaAAAAaA0AaaA0AAaAAaaaAA0a0" #coloque a chave API
bot = telebot.TeleBot(CHAVE_API)
bot.config['api_key'] = CHAVE_API
url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

while True:
    response = requests.get(url)
    if response.status_code == 200:
        valordodólar = response.json()['USDBRL']['bid']
        altadodólar = response.json()['USDBRL']['high']
        mínimadodólar = response.json()['USDBRL']['low']
        horáriododólar = response.json()['USDBRL']['create_date']
        valordoeuro = response.json()['EURBRL']['bid']
        altadoeuro = response.json()['EURBRL']['high']
        mínimadoeuro = response.json()['EURBRL']['low']
        horáriodoeuro = response.json()['EURBRL']['create_date']
        valordobtc = response.json()['BTCBRL']['bid']
        altadobtc = response.json()['BTCBRL']['high']
        mínimadobtc = response.json()['BTCBRL']['low']
        horariodobtc = response.json()['BTCBRL']['create_date']
        enviar = (f'💵DÓLAR AMERICANO💵: \nVALOR ATUAL: R$ {valordodólar}\nALTA: R$ {altadodólar}\n'
                  f'MÍNIMA: R$ {mínimadodólar}\n'
                  f'DIA/HORÁRIO: {horáriododólar}\n'
                  f'\n💶EURO💶:\nVALOR ATUAL: R$ {valordoeuro}\nALTA: R$ {altadoeuro}\n'
                  f'MÍNIMA: R$ {mínimadoeuro}\n'
                  f'DIA/HORÁRIO: {horáriodoeuro}\n'
                  f'\n💰🅱️BITCOIN🅱️💰:\nVALOR ATUAL: R$ {valordobtc}\nALTA: R$ {altadobtc}\n'
                  f'MÍNIMA: R$ {mínimadobtc}\n'
                  f'DIA/HORÁRIO: {horariodobtc}')
        print(enviar)
        bot.send_message(telegram_destino, enviar)
    else:
        print('Erro ao encontrar o valor do euro!')
    sleep(60) #edite aqui o tempo que o bot levará para mandar novas mensagens
