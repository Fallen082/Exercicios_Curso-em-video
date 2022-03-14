""" Mostrar o Primeiro e Ultimo Nome do Usuário"""

def Nome(name):
  """
  name = O Nome da qual será retirado o primeiro e ultimo nome"""
  nomezin = name.split(' ')
  return f'O seu Primeiro nome é \033[92m{nomezin[0]}\033[m, e o Ultimo é \033[92m{nomezin[-1]}\033[m]'


while True:
    usuario = str(input('Digite Aqui Seu Nome completo: '))
    # a Variavel 'a' é usada para ajudar no tratamento de alfanumericos
    a = usuario.replace(' ', '')
    # Caso o usuario não n digite nada  coloca um espaço para cair no tratamento de erro
    if usuario == '':
        usuario = usuario.replace('', ' ')
    
    # tratamento de erro para tentar não haver falhas    
    if a.isalnum() or usuario.isspace() or usuario.isnumeric():
        print('\033[92mDigite Um Nome Válido\033[m')
        continue
    else:
        # A função de mostra o primeiro e ultimo nome sendo executada
        print(Nome(usuario))
        break
