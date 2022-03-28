from UtilidadesCeV.Menu import *

bd = "Exercicio 115.txt"

if not Arq_existe(bd):
    Arq_criar(bd)

telas.menu_init(bd)
