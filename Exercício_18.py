"""Calcular Seno Cosseno e Tangente """

def cos_sen_tan(grau=0):
    """
    --> Está função irá retornar um pequeno texto mostrando
     o Seno, Cosseno e a Tangente do angulo em Graus
    :param grau: o grau do ángulo no formato int()
    :return: uma str() com as informações colocadas em cima"""
    from math import cos, tan, sin, radians

    print(f'''
     Cosseno de {grau}° é : {cos(radians(grau)):.2f}
        Seno de {grau}° é : {sin(radians(grau)):.2f}
    Tangente de {grau}° é : {tan(radians(grau)):.2f}''')


while True:
    try:
        num = int(input('Quantos Graus é o ângulo: ').strip())
        cos_sen_tan(num)
        break

    except:
        print('Valor Informado É Invalido')
