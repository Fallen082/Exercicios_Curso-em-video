from datetime import datetime

Pessoa = {}
contribucao = 0

Pessoa['Nome'] = str(input('Qual seu nome: ')).strip().title()
sexo = str(input('Qual seu sexo [M / F] : ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Qual seu sexo [M / F] : ')).strip().upper()[0]
if sexo == 'M':
    contribucao = 35
else:
    contribucao = 30

ano_nasc = str(input('Qual ano você nasceu: '))
while not ano_nasc.isnumeric():
    print('opção invalida \033[91m...\033[m')
    ano_nasc = str(input('Qual ano você nasceu: '))
ano_nasc = int(ano_nasc)
while ano_nasc > datetime.now().year:
    print('opção invalida \033[91m...\033[m')
    ano_nasc = str(input('Qual ano você nasceu: '))
Pessoa["Idade"] = datetime.now().year - ano_nasc
Pessoa["CTPS"] = str(input('Sua carteira de trabalho \033[92m[0 caso não tenha] : \033[m'))
if Pessoa["CTPS"] != '0':
    ano_contratacao = str(input('Ano de contratação: ')).strip()
    while not ano_contratacao.isnumeric():
        print('opção invalida \033[91m...\033[m')
        ano_contratacao = str(input('Ano de contratação: ')).strip()
    Pessoa["Contratação"] = int(ano_contratacao)
    Salario = str(input('Qual seu salario: R$')).strip()
    while not Salario.isnumeric():
        print('opção invalida \033[91m...\033[m')
        Salario = str(input('Qual seu salario: R$')).strip()
    Pessoa["Salario"] = Salario
    Pessoa["Aposentadora"] = (Pessoa["Contratação"]) - int(ano_nasc) + contribucao
else:
    Pessoa["CTPS"] = '\033[91mNão Tem\033[m'
print('=-'* 20)
for K, I in Pessoa.items():
    print(f'{K} é {I}')
