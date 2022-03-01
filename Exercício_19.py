from random import choice


def Alunos(quantidade=0):
    lista_al = list()
    for al in range(1, quantidade + 1):
        while True:
            nome = str(input(f'Digite O nome Do {al}º Aluno:')).strip()
            if not nome.isalpha():
                print('\033[91mDados Invalidos\033[m, Tente novamente')
            else:
                lista_al.append(nome)
                break
    return lista_al


while True:
    try:
        quant = int(input('de Quantos Alunos deseja fazer o sorteio: ').strip())
        a = Alunos(quant)
    except ValueError:
        print('\03391mInsira Um Valor Válido\033[m')
    else:
        print(f'\nO aluno escolhido foi {choice(a)}')
        break

      
      
