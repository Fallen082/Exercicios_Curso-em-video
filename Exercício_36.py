"""Verificar Se Um Empréstimo é possivel"""


def emprest(valor, salario, tempo):
    if valor / tempo > (salario * (30 / 100)):
        return '\033[91m\nInfelizmente não é possivel realizar este emprestimo\033[m'
    else:
        return '\033[92m\nÉ possivel sim realizar este emprestimo\033[m'


while True:
    try:
        quantidade = float(input('Qual o valor que você precisa R$ :').strip().replace(',', '.'))
        emprego = float(input('Quanto você recebe por mês R$ : '.strip().replace(',', '.')))
        ano = int(input('Em Quantos Anos Planeja Fazer o pagamento:'.strip()))
    except:
        print('\033[91mTente Novamente, Você digitou um valor inválido\n\033[m')
    else:
        print(emprest(quantidade, emprego, ano))
        break
