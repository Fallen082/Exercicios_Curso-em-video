"""Ver o Maior e Menor Valor"""


numeros = list()
for i in range(1, 4):
    while True:
        try:
            valor = int(input(f'{i}º Valor: ').strip())
        except (ValueError, IndexError):
            print('\033[91mValor inválido tente novamente\033[m')
        else:
            numeros.append(valor)
            break

print(f'\nDos Valores \033[96m{numeros}\033[m\n')
print(f'O maior foi:\033[92m {max(numeros)}\033[m')
print(f'O menor foi:\033[93m {min(numeros)}\033[m')
