"""Calcular média de um aluno"""


def estado(nota_final):
    if nota_final >= 7:
        print('Você está \033[92mAPROVADO\033[m')
    elif 5 < nota_final < 7:
        print('Precisa estudar mais você está de \033[93mRECUPERAÇÃO\033[m')
    else:
        print('Infelizmente você está \033[91mREPROVADO\033[m')


notas = list()
while True:
    try:
        quant = int(input('Quantas notas deseja calcular?').strip())
        print('\033[96m=-\033[m' * 18)
    except:
        print('\033[91mDigite um valor válido\033[m')
        print('\033[96m=-\033[m' * 18)
    else:
        for cois in range(1, (quant + 1)):
            while True:
                try:
                    nota = int(input(f'Qual a {cois}º Nota:').strip())
                    print()
                except:
                    print('\033[91mDigite um valor válido\033[m')
                else:
                    notas.append(nota)
                    break
        media = sum(notas) / len(notas)
        print(f'\033[94m{notas}\033[m')
        print(f'Com as notas acima sua média é \033[94m{media}\033[m\n')
        estado(media)
        break
