time = []
jogador = dict()
gols = list()
total = 0

while True:
    jogador["Nome"] = str(input('Nome Do Jogador: ')).strip()
    jogos = str(input(f'Quantos jogos o {jogador["Nome"]} já jogou: ')).strip()
    while not jogos.isnumeric():
        jogos = str(input(f'Quantos jogos o {jogador["Nome"]} já jogou: ')).strip()
    jogos = int(jogos)
    for match in range(1, jogos + 1):
        pontos = str(input(f"Quantos Gols fora feito no {match}º jogo: ")).strip()
        while not pontos.isnumeric():
            pontos = str(input(f"Quantos Gols fora feito no {match}º jogo: ")).strip()
        pontos = int(pontos)
        gols.append(pontos)
        total += pontos
    jogador["Gols"] = gols
    jogador["Total"] = total
    time.append(jogador.copy())

    confirm = str(input('Deseja continuar: [S / N]')).strip().upper()[0]
    while confirm not in 'SN':
        print('Opção Invalida \033[95m[S / N]\033[m')
        confirm = str(input('Deseja continuar: [S / N]')).strip().upper()[0]
    if confirm == 'N':
        break
    elif confirm == 'S':
        gols.clear()
        total = 0

print('\n' * 20)
while True:
    print('Numº | Nome        Gols        Total')
    for cod, valor in enumerate(time):
        print(f'  {cod}  | {valor["Nome"]}          {valor["Gols"]}         {valor["Total"]}')
    print('==' * 15)
    choice = str(input("Qual jogador deseja ver os detalhes: [999 pra parar]"))
    if choice == '999':
        break

    elif int(choice) >= len(time):
        print('Não há nenhum jogafor com este código')
    else:
        print('\n' * 15)
        print(f'Dados do jogador {time[int(choice)]["Nome"]}')
        for jogo, valor in enumerate(time[int(choice)]["Gols"]):
            print(f'no {1 + jogo}º jogo foi feito {valor} gols')


