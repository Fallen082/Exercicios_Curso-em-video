"""Analizador de nomes"""

name = str(input('Digite seu nome completo:').strip())
nome_separado = name.split(' ')
nome_junto = ''.join(nome_separado)

print(f"""
Seu nome em MAIUSCULO é: {name.upper()}
Seu nome em minusculo é : {name.lower()}
Ao Todo seu nome tem {len(nome_junto)} Letras
E o Seu Nome {nome_separado[0]} Tem {len(nome_separado[0])} Letras
""")
