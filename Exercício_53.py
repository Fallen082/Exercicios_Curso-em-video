"""Detector de Palindromo"""

nome_init = str(input('Digite Aqui Uma frase: ')).strip().upper()
print(nome_init[-1:0:-1]+ nome_init[0].strip())