Largura = str(input("Qual a \033[92mLargura\033[m da sua parede:")).replace(',', '.')
Largura = float(Largura)
Altura = str(input("Qual a \033[96maltura\033[m da sua parede:")).replace(',', '.')
Altura = float(Altura)

area = Largura * Altura

print(f'Sua parede Tem as dimensões de {Largura}x{Altura} e sua área é: {area:.2f}m²')

print(f'Para pintar sua parede será necéssario \033[92m{area / 2:.2f}\033[m Litros de Tinta')
