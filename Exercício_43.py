"""Calcular IMC do Usuário"""


def IMC(alt=0.0, pes=0.0):
    imc = pes / (alt * alt)
    print(f'o seu \033[93mIMC\033[m é : \033[92m{imc:.2f}\033[m'.replace('.', ','))
    if imc < 18.5:
        print('\033[91mCuidado\033[m, Seu PESO ESTÀ ABAIXO DO NORMAL!!')
    elif 18.5 <= imc <= 25:
        print('\033[92mParábens\033[m, Você está num PESO IDEAL')
    else:
        print('\033[91mCuidado\033[m,você ESTÀ ACIMA DO PESO!!')


while True:
    try:
        peso = float(input('Qual o Seu Peso \033[94m(KG)\033[m: ').strip().replace(',', '.'))
    except:
        print('\033[91mDigite um valor válido\033[m')
        continue
    try:
        altura = float(input('Qual sua Altura em \033[94m(M)\033[m: ').strip().replace(',', '.'))
    except:
        print('\033[91mDigite um valor válido\033[m')
        continue
    IMC(altura, peso)
    break
