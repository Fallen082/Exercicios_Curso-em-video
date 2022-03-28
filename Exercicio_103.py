def jogador(jog='<desconhecido>', gol=0):
    a = f"O Jogador {jog}, fez {gol} gols durante o campeonato"
    return a

nome = input('Qual o nome:')
gols = input('Quantos gols')
if nome == '' and gols == '':
    print(jogador())

elif gols == '':
    print(jogador(nome))

elif nome == '':
    try:
        print(jogador(gol=int(gols)))
    except:
        print(jogador())

else:
    try:
        print(jogador(nome, int(gols)))
    except:
        print(jogador(nome))

