"""Conversor de bases númericas"""


def line(quantidade):
    print('=' * quantidade)


def title(txt):
    line((len(txt) + 4))
    print(txt.center(len(txt) + 4))
    line((len(txt) + 4))


while True:
    try:
        valor = int(input('Digite aqui o Número Inteiro: ').strip())
    except:
        print('\033[91mDigite um valor válido\033[m')
    else:
        while True:
            try:
                title("Converter Para Qual Base")
                print('\033[94m[1]\033[m = Bínario \n\033[94m[2]\033[m = Octal \n\033[94m[3]\033[m = Hexadecimal')
                line(28)
                escolha = int(input('\033[92mOpção: \033[m').strip())
                line(28)
            except:
                print('\033[91mDigite um valor válido\033[m')
            else:
                if escolha not in range(1, 4):
                    print('\033[91mDigite um valor válido\033[m')
                    continue
                elif escolha == 1:
                    print(f'Valor Convertido : {bin(valor)}')
                    break
                elif escolha == 2:
                    print(f'Valor Convertido : {oct(valor)}')
                    break
                else:
                    print(f'Valor Convertido : {hex(valor)}')
                    break

        break
