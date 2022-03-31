def int_input():
    num = 'noting'
    while not num.isnumeric():
        num = input('Digite algum número: ')
        if not num.isnumeric():
            print('\033[91mVocê não digitou um número tente novamente\033[m')
        else:
            return num


n = int_input()
print(f'\nO número escolhido foi {n} :)')
