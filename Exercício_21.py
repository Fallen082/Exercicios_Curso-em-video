"""Leitor de Música"""

def tocar_musica(arquivo):
  """
  O Arquivo Informado Precisa estar em formato (.wav)"""
  import simpleaudio as sa
  print('\033[91mTocando...\033[m')
  musica = sa.WaveObject.from_wave_file(arquivo)
  Play_music = musica.play()
  Play_music.wait_done()


lista = ['a_music\Céu_Azul.wav', 'a_music\Dona_morte.wav']
while True:
  print('¬'* 27)
  print('Musicas'.center(27))
  print('¬'* 27)
  print('[1] = \033[94mCéu Azul\033[m [Cover Feio]')
  print('[2] = \033[91mDona Morte\033[m')
  print('¬'* 27)
  while True:
    try:
      escolha = int(input('Digite a Opção Escolhida: ').strip())
    except (ValueError , TypeError, IndexError):
      print('\033[91mdigite uma Opção valida\033[m')
    if escolha == 1 or 2:
      print('\033[93mIrei Tocar a Música agora\033[m')
      tocar_musica(lista[escolha - 1])
      break
    elif escolha == 999:
      break
      break
    else:
      print('erro')
    
