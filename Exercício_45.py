"""Jogo Pedra, Papel, Tesoura"""

from random import choice

def game(jogador, certa):
  if jogador == "PEDRA":
    if certa == "PEDRA":
      print('Computador jogou PEDRA, \033[96mVocê EMPATOU\033[m')
    elif certa == "PAPEL":
      print('Computador jogou PAPEL, \033[91mVocê PERDEU\033[m')
    elif certa == "TESOURA":
      print('Computador jogou TESOURA, \033[92mVocê GANHOU\033[m')
      
  elif jogador == "PAPEL":
    if certa == "PEDRA":
      print('Computador jogou PEDRA, \033[92mVocê GANHOU\033[m')
    elif certa == "PAPEL":
      print('Computador jogou PAPEL, \033[96mVocê EMPATOU\033[m')
    elif certa == "TESOURA":
      print('Computador jogou TESOURA, \033[91mVocê PERDEU\033[m')
      
  elif jogador == "TESOURA":
    if certa == "PEDRA":
      print('Computador jogou PEDRA, \033[91mVocê PERDEU\033[m')
    elif certa == "PAPEL":
      print('Computador jogou PAPEL, \033[92mVocê GANHOU\033[m')
    elif certa == "TESOURA":
      print('Computador jogou TESOURA, \033[96mVocê EMPATOU\033[m')
      


elementos = ["PEDRA", "PAPEL", "TESOURA"]
while True:
  resposta = choice(elementos)
  print('='* 13)
  print(" [1] \033[95mPedra\033[m\n [2] \033[95mPapel\033[m\n [3] \033[95mTesoura\033[m")
  print('='* 13)
  
  while True:
    try:
      player = int(input("OPÇÃO: ").strip())
    except:
      print('\033[91mDigite uma informação válida\033[m')
    else:
      if player not in range(1, 4):
        print('\033[91mDigite uma informação válida\033[m')
      else:
        if player == 1:
          player = "PEDRA"
          
        elif player == 2:
          player = "PAPEL"

        else:
          player = "TESOURA"
          
        game(player, resposta)
        break
        
  while True:
    try:
      confirm = str(input('Deseja Jogar Novamente \033[94m[S/N]\033[m: ')).upper()
    except:
      print('\033[91mDigite uma informação válida\033[m')
    else:
      if confirm not in "SN":
        print('\033[91mDigite uma informação válida\033[m')
        continue
      else:
        break
  if confirm == "N":
    print('\033[92mFoi Bom Jogar Com Você, Tchau-Tchau\033[m')
    break
