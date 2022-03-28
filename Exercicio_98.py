from time import sleep as sl


def contador(Inicio, Fim, Passos):
    if Inicio > Fim:
        if Passos == 0 or '':
            Passos = 1
        if Passos < 0:
            Passos = Passos * (-1)
        print('==' * 20)
        print(f'Contando de {Inicio} até {Fim} de {Passos} em {Passos}')
        while Inicio >= Fim:
            print(f'{Inicio} ', end='')
            Inicio = Inicio - Passos
            sl(.3)
        print('FIM!')
    elif Inicio < Fim:
        if Passos == 0 or '':
            Passos = 1
        if Passos < 0:
            Passos = Passos * (-1)
        print('==' * 20)
        print(f'Contando de {Inicio} até {Fim} de {Passos} em {Passos}')
        while Inicio <= Fim:
            print(f'{Inicio} ', end='')
            Inicio = Inicio + Passos
            sl(.3)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('==' * 20)
print('Agora Faça você mesmo a contagem :)')
contador(int(input('Qual O Inicio: ')), int(input('Qual O Fim: ')), int(input('De quantos em Quantos passos: ')))




