import ply.yacc as yacc
from calculadora_lex import tokens, literals
import sys

def produtorio(lista):
    prod = 1
    for i in lista:
        prod = prod * i
    return prod

def somatorio(lista):
    prod = 0
    for i in lista:
        prod = prod + i
    return prod
    
def p_Z(p):
    "Z : Exp"
    print(p[1])


def p_Exp_Add(p):
    "Exp   : '(' '+' Lista Exp ')'"
    p[0] = somatorio(p[3]) + p[4]

def p_Exp_Mul(p):
    "Exp   : '(' '*' Lista Exp ')'"
    p[0] = produtorio(p[3]) * p[4]

#------------------------------------------------------------

def p_Exp_Num(p):
    "Exp   : num"
    p[0] = p[1]

def p_Lista(p):
    "Lista  :  Lista Exp"
    p[0] = p[1] + [p[2]]

def p_Lista_Elem(p):
    "Lista  :  Exp"
    p[0] = [p[1]]

def p_error(p):
    print('Erro sintatico: ',p)
    parser.sucess = False

parser = yacc.yacc()
parser.res = 0

for linha in sys.stdin:
    parser.sucess = True
    parser.parse(linha)
