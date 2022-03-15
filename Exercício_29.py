"""Simulador de Radar de Trânsito"""

def radar(velocidade=0):
  """
  Está Função Vai retornar de acordo com a velocidade se o motorista será multado ou não"""
  while True:
    if velocidade > 80:
      multa = (velocidade - 80) * 7 
      return f"""\033[91mVocê ultrapassou o limite de velocidade.
      Percorrendo á {velocidade} Km/h
      Valor da multa é {multa:.2f}R$\033[m""".replace('.', ',')
    else:
      return """\033[92mVocê está dentro dos limites tenha um bom dia\033[m"""


while True:
  try:
    km = int(input('Você está a quantos Km/h: '))
  except (ValueError, IndexError):
    print('\033[91mERRO\033[m')
  else:
    if km < 0:
      print('\033[91mQuilometragem Inválida\033[m')
    else:
      print(radar(km))
    
    
    
