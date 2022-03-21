"""Soma de todos os números impares multiplos de 3"""

def total_li(quantidade=0):
    lista= list()
    for item in range(1,quantidade + 1):
        if item % 2 != 0 and item % 3 == 0:
            lista.append(item)
    return lista
    
while True:
    try:
        distancia = int(input('Quantos números deseja analizar:').strip())
    except:
        print('\033[91mDigite um valor válido\033[m')
    else:
        a= total_li(distancia)
        print(f'O Valor Total dos \033[94m{len(a)}\033[m números analizados é: \033[94m{sum(a)}\033[m')
        break
