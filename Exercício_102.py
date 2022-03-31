def Factor(num, mostrar=False):
    """
    --> Mostra a fatorial do numero recebido
    :param num: O Número que será feito a fatorial
    :param mostrar: Se quer que mostre o passo a passo ou não
    :return: mostra o valor da fatorial de num
    """
    tot = 1
    if mostrar:
        for item in range(num, 0, -1):
            if item == 1:
                print(item, end=' = ')
                tot = tot * item
            else:
                print(item, end=' x ')
                tot = tot * item
    else:
        for item in range(num, 0, -1):
            tot = tot * item

    print(tot)


while True:
    print('==' * 24)
    try:
        num = int(input('Digite aqui um número para ver sua fatorial: '))
        ver = str(input('Deseja Ver Passo a passo? [S/N]').strip().upper())[0]
        if ver == 'S':
            ver = True
        else:
            ver = False
        break
    except:
        print('Algo deu errado Tente NOVAMENTE')
help(Factor)
Factor(num, ver)
