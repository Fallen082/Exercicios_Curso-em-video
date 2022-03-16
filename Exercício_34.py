"""Aumento Salarial"""


def aumento(salario=0.0):
    if salario <= 1250:
        return salario + (salario * (15 / 100))
    else:
        return salario + (salario * (10 / 100))


while True:
    try:
        valor = str(input('Digite Aqui O valor do seu sálario atual R$ : ').strip().replace(',', '.'))
        valor = float(valor)
        print(
            f'Quem Recebia {valor:.2f} agora com o aumento salarial vai receber {aumento(valor):.2f}'.replace('.', ','))
    except:
        print('\033[91mDigite Um Valor Válido\033[m')
