notas = []
notas_f = list()


def acrescentador(nome_aluno, nota_1, nota_2, media_aluno):
    notas.append(nome_aluno)
    notas.append(nota_1)
    notas.append(nota_2)
    notas.append(media_aluno)
    notas_f.append(notas[:])
    notas.clear()


while True:
    print('\033[93m=\033[92m-\033[94m=\033[95m-\033[m' * 13)
    nome = str(input('Digite aqui seu Nome: ').strip())
    nota1 = float(input('Qual foi a \033[97mPrimeira\033[m nota: ').strip().replace(',', '.'))
    nota2 = float(input('Qual foi a \033[97mSegunda\033[m nota: ').strip().replace(',', '.'))
    media = (nota1 + nota2) / 2
    acrescentador(nome, nota1, nota2, media)

    confirm = str(input('Deseja Continuar [S/N]: ').strip().upper())[0]
    while confirm not in 'SN':
        print('\03391mOpção Invalida\033[m')
        confirm = str(input('Deseja Continuar [S/N]: ').strip())[0]
    if confirm == 'N':
        break
print('\033[93m=\033[92m-\033[94m=\033[95m-\033[m' * 13)
print()

print('==' * 10)
print('Nº    Nome    Média')
pos = 0
for aluno in notas_f:
    print(f'\033[97m{pos}º   {aluno[0]}    {aluno[3]}\033[m')
    pos += 1
print('==' * 10)

while True:
    qual = str(input('Deseja ver a nota de qual aluno: [type 999 for stop]: ').strip())
    while not qual.isnumeric():
        print('\03391mOpção Invalída\033[m')
        qual = str(input('Deseja ver a nota de qual aluno:  [type 999 for stop]: ').strip())
    qual = int(qual)
    if qual == 999:
        break
    if qual <= len(notas_f) - 1:
        print(f'{notas_f[qual][0]}, {notas_f[qual][1]} , {notas_f[qual][2]}')

    else:
        print('\033[91mOpção Invalída\033[m')
