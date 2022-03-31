"""def area():
    largura = float(input("Digite Aqui A Largura Do Retangulo: ").strip().replace(',', '.'))
    comprimento = float(input("Digite Aqui O Comprimento Do Retangulo: ").strip().replace(',', '.'))
    print(largura * comprimento)"""


def area(Largura, Comprimento):
    resp = Largura * Comprimento
    return f'{resp:.2f}'


larg = float(input("Digite Aqui A Largura Do Retangulo Em Metros: ").strip().replace(',', '.'))
compr = float(input("Digite Aqui O Comprimento Do Retangulo Em Metros: ").strip().replace(',', '.'))
print('===' * 28)
print(f"A area de um retangulo com {larg:.2f} de largura e {compr:.2f} de comprimento é :: {area(larg, compr)} M²")
print('===' * 28)
