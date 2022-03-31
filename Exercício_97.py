def Tracin(palavra):
    print('~' * (len(palavra) + 4))
    print('  {}  '.format(palavra))
    print('~' * (len(palavra) + 4))


while True:
    text = str(input('Qual palavra deseja ver: [999 para parar]'))
    if text == '999':
        break
    else:
        print('\n' * 2)
        Tracin(text)
        print('\n' * 2)

