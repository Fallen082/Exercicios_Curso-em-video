Aluno = dict()
lista_alunos = list('')

while True:
    print('=-' * 14)
    Aluno["Nome"] = str(input('Qual Seu Nome:')).title()
    Aluno["Média"] = float(input('Qual sua Média:').replace(',', '.'))

    if Aluno["Média"] >= 7:
        Aluno["Status"] = 'Aprovado'
    elif 5 <= Aluno["Média"] < 7:
        Aluno["Status"] = 'Recuperação'
    else:
        Aluno["Status"] = '\033[91mReprovado\033[m'

    lista_alunos.append(Aluno.copy())
    Aluno.clear()

    confirm = str(input('\nDeseja Acrescentar mais alguem?')).upper()[0]
    while confirm not in 'SN':
        confirm = str(input('\nDeseja Acrescentar mais alguem?')).upper()[0]
    if confirm == 'N':
        break

print()
print('\n|   Nome   | Média |  Status  |')
for listas in lista_alunos:
    for coisa in listas.values():
        print(f"| {coisa}    ", end='')
    print()
