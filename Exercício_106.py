def MenuHelper(func):
    try:
        texto = help(func)
        return texto
    except:
        print('Ocorreu Algum erro, talvez na tenha esta função no sistema')


while True:
    funcao = str(input('Digite o nome da função que deseja ver uma explicação \033[92m[FIM] para parar: \033[m'))
    if funcao.upper() == 'FIM':
        break
    else:
        MenuHelper(funcao)

