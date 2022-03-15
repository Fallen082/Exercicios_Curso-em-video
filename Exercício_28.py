"""Um Jogo de Advinhação"""

def title(text):
    print("="* (len(text) + 23))
    print(text.center(len(text) + 23))
    print("="* (len(text) + 23))
    
    
def randomize(init=0, end=0):
    from random import randint
    value = randint(init, end)
    return value
    

while True:
  
    wrong_numb = list()
    title('Jogo De Advinhação')
    value = randomize(1, 10)
    print("Pensei um número \033[92m[1 a 10]\033[m, Tente Advinhar")
    while True:
        
        print()
        try:
          print(f'Errados: \033[91m{wrong_numb}\033[m')
          choice = int(input('Digite Aqui O Valor: '))
        except ValueError:
            print('\n\033[91mDigite Um Valor Válido\033[m')
            continue
        else:
          if choice != value:
            wrong_numb.append(choice)
            print('\033[91mErrado\033[m')
            continue
          else:
            print(f'\033[92mParabéns Você acertou \033[94m[{choice}] \033[92mcom {len(wrong_numb) + 1} Tentativas\033[m')
            
            while True:
              try:
                again = str(input('Deseja Jogar Novamente [S/N]:').strip().upper())[0]
                if again not in 'NS':
                  print('\033[91mOpção Inválida\033[m')
                  continue

              except IndexError:
                print('\033[91mOpção Inválida\033[m')
              else:
                if again == "N":
                  break
                else:
                  break
        break
    if again == "N":
      break
