"""Ver se o número é par ou impar"""

def title(msg):
  print('='*(len(msg)+ 13))
  print(msg.center(len(msg) + 13))
  print('='*(len(msg)+ 13))


title("Par ou Impar")
while True:
  try:
    numb = int(input('Digite um número: '))
  except (ValueError, IndexError):
    print('\033[91mDigite um valor válido\033[m')  
  else:
    if numb % 2 !=0:
      print("O número digitado é \033[95mImpar\033[m")
      break
    else:
      print("O número digitado é\033[95mPar\033[m")
      break
