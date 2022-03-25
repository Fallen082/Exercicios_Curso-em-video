"""Grupos de maior e menor idade"""
from datetime import datetime

maior = list()
menor = list()
ano = datetime.now().year


def mostrar_nome(lista):
    for nome in lista:
        print(nome, end=' ')
    print()

for pessoas in range(1, 8):
    while True:
        try:
            nome = input(f"Qual o Nome da \033[94m{pessoas}º\033[m Pessoa: ").strip().title()
            nascimento = int(input(f"Em Qual Ano a \033[94m{pessoas}º\033[m Nasceu:").strip())
        except:
            print('\033[91mDigite um número válido\033[m')
        else:
            if ano - nascimento >=18:
                maior.append(nome)
                break
            else:
                menor.append(nome)
                break

print(f"Ao Todo há {len(maior)} Pessoas maiores de idade sendo elas : {maior}")
print(f"E por fim há {len(menor)} Pessoas menores de idade sendo elas : {menor}")