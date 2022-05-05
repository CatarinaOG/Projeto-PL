import ply.yacc as yacc
from TP2_lex import tokens
import sys

flex = open("lex.py","a")
fyacc = open("yacc.py","a")


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
    parser.literals = p[3]


#-------------------------------------------TOKENS----------------------------------------------
def p_LEXES_TOKENS(p):
    "LEXES : tokens equal oBracket LISTTOKENS cBracket LEXES "

def p_LISTTOKENS(p):
    "LISTTOKENS : prime token prime CONTLISTTOKENS"
    parser.tokens.append(p[2])

def p_CONTLISTTOKENS(p):
    "CONTLISTTOKENS : comma prime token prime CONTLISTTOKENS "
    parser.tokens.append(p[3])

def p_CONTLISTTOKENS_EMPTY(p):
    "CONTLISTTOKENS : "
    

#-------------------------------------------IGNORE----------------------------------------------

def p_LEXES_IGNORE(p):
    "LEXES : ignor equal listignore LEXES"
    flex.write("\nt_ignore = "+p[3])

#--------------------------------------------ExpDefs-----------------------------------------------

def p_LEXES_EXPDEF(p):
    "LEXES : er expReg expDef LEXES"
    parser.expReg.append(p[2])
    parser.expDef.append(p[3])

#--------------------------------------------EMPTY LEX-----------------------------------------------


def p_LEXES_EMPTY(p):
    "LEXES : "


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
parser.tokens = []
parser.literals = ""
parser.expReg = []
parser.expDef = []

parser.parse(sys.stdin.read())