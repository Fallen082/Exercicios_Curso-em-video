"""Contar a quantidade de uma letra especifica dentro de alguma frase

def contador(letra, frase):
    """
    letra == o objeto que ele está contando
    frase == o local onde ele vai procurar a letra informada
    """
   
    if frase.find(letra) > -1:
        frase = frase.upper()
        letra = letra.upper()
        quantidade = frase.count(letra)
        primeira = frase.find(letra)
        ultima = frase.rfind(letra)
        
        return\
        f"""Dados sobre a letra {letra.upper()}:
        Essa letra apareceu {quantidade} Vezes
        A Primeira vez que apareceu foi na {primeira +1} posição
        A Ultima Vez que apareceu foi na {ultima +1} posição
        """
    else:
        return f"Não há letra {letra} na frase informada"
        
    
frase = str(input('Informe Alguma Frase: ')).strip()
letra = str(input('Qual Letra Deseja Procurar: ')).strip()
print(f'\n{contador(letra, frase)}')
