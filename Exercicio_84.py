todos = []
acima = []
na_media = []
abaixo = []
cont = 0

while True:
    print('\033[93m=\033[92m-\033[94m=\033[95m-\033[m' * 9)
    nome = str(input('Digite Seu nome: ').strip().title())
    altura = float(input('Digite Aqui sua altura em Metros:  ').strip().replace(',', '.'))
    peso = float(input('Digite Aqui seu peso em Quilos: ').strip().replace(',', '.'))
    imc = peso / (altura * altura)
    todos.append(nome), todos.append(peso), todos.append(imc)
    cont += 1
    if imc < 18.5:
        abaixo.append(todos[:])
    elif imc <= 24.99:
        na_media.append(todos[:])
    elif imc >= 25:
        acima.append(todos[:])
    todos.clear()
    confirm = str(input('Deseja continuar? \033[91m[S/N]\033[m : ').strip().upper())[0]
    while confirm not in 'SN':
        print('Opção Invalída \n')
        confirm = str(input('Deseja continuar? \033[91m[S/N]\033[m : ').strip().upper())[0]

    if confirm == 'N':
        print('\033[93m=\033[92m-\033[94m=\033[95m-\033[m' * 9)
        break

print(f'Foram cadastradas no total {cont} Pessoas')
print(f'{len(acima)} Estão acima do peso sendo elas ', end='')
for coisa in acima:
    print(f'\033[95m{coisa[0]}\033[m com {coisa[1]} Quilos //', end=' ')
print()

print(f'{len(na_media)} Estão no peso ideal sendo elas ', end='')
for coisa in na_media:
    print(f'\033[95m{coisa[0]}\033[m com {coisa[1]} Quilos //', end=' ')
print()

print(f'{len(abaixo)} Estão abaixo do peso sendo elas ', end='')
for coisa in abaixo:
    print(f'\033[95m{coisa[0]}\033[m com {coisa[1]} Quilos //', end=' ')
print()
