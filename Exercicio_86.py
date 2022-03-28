coluna = []
matriz = list()

print('\033[93m=\033[92m-\033[94m=\033[95m-\033[m' * 13)
for linhas in range(0, 3):
    for colunas in range(0, 3):
        coluna_fun = str(input(f'Digite um Número inteiro para a posição \033[97m[{linhas}/{colunas}]\033[m').strip())
        while not coluna_fun.isnumeric():
            print('\033[91mOpção Invalida\033[m')
            coluna_fun = \
                str(input(f'Digite um Número inteiro para a posição \033[97m[{linhas}/{colunas}]\033[m').strip())
        coluna.append(coluna_fun)
    matriz.append(coluna[:])
    coluna.clear()
print('\033[93m=\033[92m-\033[94m=\033[95m-\033[m' * 13)
for item in matriz:
    print(f'[{item[0]}] [{item[1]}] [{item[2]}]')

print('\033[93m=\033[92m-\033[94m=\033[95m-\033[m' * 13)

