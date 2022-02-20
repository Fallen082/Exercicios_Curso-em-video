Var_dis = input('Digite algo aqui: ')

print(f' O tipo da Variavel digitada é {Var_dis.type()}')
print(f'''
      Há Somente espaços? {Var_dis.isspace()}
       É Somente números? {Var_dis.isnumeric()}
      Há Somente letras? {Var_dis.isalpha()}
      Há Letras e Números? {Var_dis.is.alnum()}
      Está em Maiusculo? {Var_dis.isupper()}
      Está em Minusculo? {Var_dis.islower()}
      Está Capitalizada? {Var_dis.iscapitalize()}'''
