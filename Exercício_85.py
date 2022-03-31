numeros = [[], []]

for num in range(1, 8):
    Numb = str(input(f'Digite aqui o \033[9{num}m{num}\033[mº da lista:').strip())
    while not Numb.isnumeric():
        Numb = str(input(f'Digite aqui o \033[9{num}m{num}\033[mº da lista:').strip())
    Numb2 = int(Numb)
    if Numb2 % 2 == 0:
        numeros[0].append(Numb2)
    else:
        numeros[1].append(Numb2)
print()
print(f'Esses foram os números Pares da lista : {sorted(numeros[0])}')
print()
print(f'Esses foram os números Impares da lista : {sorted(numeros[1])}')
