pessoa = dict()
lista = list()
idade = 0

while True:
    pessoa["Nome"] = str(input('Digite Aqui Seu nome:')).title().strip()

    pessoa["sexo"] = str(input('Qual seu Sexo [M / F]')).strip().upper()[0]
    while pessoa["sexo"] not in 'FM':
        print('Opção Invalida \033[95m[M / F]\033[m')
        pessoa["sexo"] = str(input('Qual seu Sexo [M / F]')).strip().upper()[0]

    pessoa["Idade"] = str(input('Digite Sua Idade: ')).strip()
    while not pessoa["Idade"].isnumeric():
        print('Opção Invalida')
        pessoa["Idade"] = str(input('Digite Sua Idade: ')).strip()
    pessoa["Idade"] = int(pessoa["Idade"])
    idade += pessoa["Idade"]
    confirm = str(input('Deseja continuar: [S / N]')).strip().upper()[0]
    while confirm not in 'SN':
        print('Opção Invalida \033[95m[S / N]\033[m')
        confirm = str(input('Deseja continuar: [S / N]')).strip().upper()[0]
    lista.append(pessoa.copy())
    print('===' * 20)
    if confirm == 'N':
        break
print('\n' * 25)

print(f'A)    O total de pessoas cadastradas foi {len(lista)}')
print(f'B)    A média de idade das {len(lista)} pessoas é {idade / len(lista):.2f}')
print(f'C)    As garotas cadastradas foram : ', end='')
for dicionario in lista:
    if dicionario["sexo"] == 'F':
        print(f'{dicionario["Nome"]} |', end='')
print()
print(f'D)    Lista de pessoas acima da média:\n')
for dicionario in lista:
    if dicionario["Idade"] > (idade / len(lista)):
        print(dicionario)

print('\033[91m.....Encerrado.....\033[m')
