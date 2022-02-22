'''Conversor de temperaturas'''

try:
  temp = str(input('Digite aqui a Temperatura em Celsius °C : ')).replace(',','.').strip()
  Kelvin = float(temp) + 273
  fahren = (float(temp) * 1.8) + 32

  print(f'''
        {float(temp):.1f} Graus Celsius °C Equivalem a:

        {Kelvin:.1f} Graus Kelvin K
        {fahren:.1f} Graus Fahrenheit °F''')
except:
  print('\033[91mAlguma Informação foi digitada incorretamente\033[m')
finally:
  print('Encerrando Programa ...')
      
