""" Confirmar se há a palavra santo na cidade onde você nasceu"""

def confirm_Sant(palavra):
    for item in palavra:
        if item == 'SANTOS' or item == 'SANTO':
            confirm = True
            break
        else:
            confirm = False
            continue
    return confirm
        
  

nasc = str(input('Em qual cidade você nasceu: ').strip().upper())
nasc = nasc.split(' ')
print(confirm_Sant(nasc))
