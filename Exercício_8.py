'''Conversor de medidas'''

try:
  Metros = int(input('Digite uma distancia em metros:'))
  print(f'''
        Quílometro: {Metros / 1000} KM
        Hectômetro: {Metros / 100} HM
        Decâmetro : {Metros / 10} DAM
        Metro     : {Metros} M
        Decímetro : {Metros * 10} DM
        Centímetro: {Metros * 100} CM
        milímetro : {Metros * 1000} MM
        ''')

except:
  print('erro')
