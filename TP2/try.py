import ply.yacc as yacc
from TP2_lex import tokens,literals
import sys

def p_GRAMMAR(p):
    "Z : LEX"
    print("Acabou")

def p_LEX(p):
    "LEX : lex LEXES"

def p_LEXES(p):
    "LEXES : literals '=' '\"' LITERALS '\"' "

def p_LEXES_LITERALS(p):
    "LITERALS : literal LITERALS"

def p_LEXES_LIST_LIT(p):
    "LITERALS : "

def p_error(p):
    print('Erro sintatico: ',p)
    parser.sucess = False


parser = yacc.yacc()
parser.isLex = False
parser.isYacc = False

for linha in sys.stdin:
    parser.sucess = True
    parser.parse(linha)