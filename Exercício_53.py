"""Detector de Palindromo"""

nome_init = str(input('Digite Aqui Uma frase: ').upper().replace(' ', ''))
nome_final = nome_init[-1:0:-1]+ nome_init[0]
if nome_init == nome_final:
    print(f"""\033[92mEssa palavra É um palindromo:\033[m
     INICIAL: \033[96m{nome_init}\033[m  
       FINAL: \033[96m{nome_final}\033[m""")
else:
    print(f"""\033[91mEssa palavra NÃO É um palindromo:\033[m
     INICIAL: \033[96m{nome_init}\033[m  
       FINAL: \033[96m{nome_final}\033[m""")