"""Confirmar Se há silva no nome"""

def Silva(frase):
    """
    Recebe a Frase e Procura se há 'Silva' dentro da frase
    Retornando Assim ums STR
    """
    frase2 = frase.upper()
    tem = frase2.find('SILVA')
    if tem > -1:
        return "Há \033[92msim\033[m a palavra Silva em seu nome"
    else:
        return"\033[91mNão\033[m há a palavra Silva em seu nome"
        

nome = str(input('Digite Seu Nome: '))
print(Silva(nome))
