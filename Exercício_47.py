"""Contador de Pares"""


def Pares(numero):
    for numb in range(1, numero + 1):
        if numb % 2 == 0:
            print(f'|{numb}',end='|')        
        

print('#'* 44)
print('Contador de Pares'.center(44))
print('#'* 44)
while True:
    try:
        quantidade = int(input('Quantos Número Deseja Fazer a \033[92mContagem\033[m? ').strip())
    except:
        print('Digite Um Valor Válido')
    else:
        Pares(quantidade)
        break
        
