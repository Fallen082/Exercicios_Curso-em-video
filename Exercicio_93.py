jogador = dict()
gols = list()
total = 0
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

print('\n' * 25)
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'{k} é : {v}')
print('=-' * 30)
print(f'O Jogador {jogador["Nome"]} ja jogou {len(jogador["Gols"])} Partidas')
cont = 1
for partidas in jogador["Gols"]:
    print(f'   =>  Na \033[94m{cont}ª\033[m Partida foi feito \033[91m{partidas}\033[m Gol ')

    cont += 1
print(f'A quantidade total de gols foi: {jogador["Total"]}')