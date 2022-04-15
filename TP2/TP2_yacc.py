import ply.yacc as yacc
from TP2_lex import tokens
import sys

#-------------------------------------------GRAMMAR----------------------------------------------

def p_GRAMMAR(p):
    "Z : LEX YACC"
    print("Acabou")


#-------------------------------------------LEX----------------------------------------------

def p_LEX(p):
    "LEX : lex LEXES"

#-------------------------------------------LITERALS----------------------------------------------

def p_LEXES_LITERALS(p):
    "LEXES : literals equal listliterals LEXES "


#-------------------------------------------TOKENS----------------------------------------------

def p_LEXES_TOKENS(p):
    "LEXES : tokens equal oBracket LISTTOKENS cBracket LEXES "
    print(p[4])

def p_LISTTOKENS(p):
    "LISTTOKENS : token CONTLISTTOKENS"
    p[0] = [p[1]] + p[2]

def p_CONTLISTTOKENS(p):
    "CONTLISTTOKENS : comma token CONTLISTTOKENS "
    p[0] = [p[2]] + p[3]

def p_CONTLISTTOKENS_EMPTY(p):
    "CONTLISTTOKENS : "
    p[0] = []

#-------------------------------------------IGNORE----------------------------------------------

def p_LEXES_IGNORE(p):
    "LEXES : ignor equal listignore LEXES"
    print(p[3])

#--------------------------------------------EMPTY LEX-----------------------------------------------


def p_LEXES_EMPTY(p):
    "LEXES : "

def p_LEX_EMPTY(p):
    "LEX : "

#--------------------------------------------YACC-----------------------------------------------

def p_YACC(p):
    "YACC : yacc YACCS"


#-------------------------------------------PRECEDENCE----------------------------------------------

def p_YACCS_PREC(p):
    "YACCS : precedence equal oBracket LISTPRECE cBracket YACCS"
    print(p[4])

def p_LISTPRECE(p):
    "LISTPRECE : listprecedence comma LISTPRECE"
    p[0] = [p[1]] +p[3]

def p_LISTPRECE_EMPTY(p):
    "LISTPRECE : "
    p[0] = []

#verificar que é um tuplo


#--------------------------------------------EMPTY YACC-----------------------------------------------

def p_YACC_EMPTY(p):
    "YACCS : "


def p_error(p):
    print('Erro sintatico: ', p)
    parser.sucess = False




parser = yacc.yacc()
parser.isLex = False
parser.isYacc = False
parser.literals = []

for linha in sys.stdin:
    parser.sucess = True
    parser.parse(linha)