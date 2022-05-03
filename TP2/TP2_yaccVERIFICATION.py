import ply.yacc as yacc
from TP2_lex import tokens
import sys

#-------------------------------------------GRAMMAR----------------------------------------------

def p_GRAMMATICA(p):
    "Z : GRAMMAR"

def p_GRAMMAR_lex(p):
    "GRAMMAR : GRAMMAR LEX"

def p_GRAMMAR_yacc(p):
    "GRAMMAR : GRAMMAR yacc"

def p_GRAMMAR_python(p):
    "GRAMMAR : GRAMMAR python"

def p_GRAMMAR_empty(p):
    "GRAMMAR : "



#-------------------------------------------LEX----------------------------------------------

def p_LEX(p):
    "LEX : lex LEXES "

#-------------------------------------------LITERALS----------------------------------------------

def p_LEXES_LITERALS(p):
    "LEXES : literals equal listliterals LEXES"
    f = open("lex.py","a")
    f.write("\nliterals = "+p[3])
    f.close()

#-------------------------------------------TOKENS----------------------------------------------
def p_LEXES_TOKENS(p):
    "LEXES : tokens equal oBracket LISTTOKENS cBracket LEXES "
    #print(p[4])

def p_LISTTOKENS(p):
    "LISTTOKENS : token CONTLISTTOKENS"
    #p[0] = [p[1]] + p[2]

def p_CONTLISTTOKENS(p):
    "CONTLISTTOKENS : comma token CONTLISTTOKENS "
    #p[0] = [p[2]] + p[3]

def p_CONTLISTTOKENS_EMPTY(p):
    "CONTLISTTOKENS : "
    #p[0] = []
#-------------------------------------------IGNORE----------------------------------------------

def p_LEXES_IGNORE(p):
    "LEXES : ignor equal listignore LEXES"
    f = open("lex.py","w")
    f.write("\nt_ignore = "+p[3])
    f.close()

#--------------------------------------------EMPTY LEX-----------------------------------------------


def p_LEXES_EMPTY(p):
    "LEXES : "


#--------------------------------------------YACC-----------------------------------------------
"""
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
"""

def p_error(p):
    print('Erro sintatico: ', p)
    parser.sucess = False




parser = yacc.yacc()

parser.parse(sys.stdin.read())