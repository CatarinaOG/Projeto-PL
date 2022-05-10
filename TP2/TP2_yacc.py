from posixpath import split
import ply.yacc as yacc
import re
from TP2_lex import tokens
import sys

flex = open("lex.py","a")
fyacc = open("yacc.py","a")


#-------------------------------------------LITERALS----------------------------------------------

def writeLiterals(literals):
    flex.write("\nliterals = "+literals)

#-------------------------------------------IGNORE----------------------------------------------

def writeIgnore(ignore):
    flex.write("\nt_ignore = "+ignore)

#-------------------------------------------TOKENS----------------------------------------------

def tokenNameFunc(expDef):
    name = re.search("\'.+\'",expDef)
    return name.group(0).strip("\'")


def writeTokens(tokens):
    flex.write("\ntokens = [\'"+tokens[0]+"\'")
    for token in tokens[1:]:
        flex.write(",\'"+token+"\'")
    flex.write("]\n")

#-------------------------------------------EXP DEF----------------------------------------------

def writeExpDefs(parser):
    nrExp = len(parser.expDef)

    parser.expDef.reverse()
    parser.expReg.reverse()
    
    for i in range(0,nrExp):
        if parser.expReg[i] != '.':
            tokenName = tokenNameFunc(parser.expDef[i])
            flex.write("\ndef t_" + tokenName + "(t):")
            flex.write("\n  r\'" + parser.expReg[i] + "\'")
            flex.write("\n " + parser.expDef[i] + "\n")
        else:
            flex.write("\ndef t_error(t):")
            parser.expDef[i] =parser.expDef[i][7:]
            parser.expDef[i] =parser.expDef[i][:-2]
            sizeExp = len(parser.expDef[i])
            
            while sizeExp > 0:
                errorPrint = re.match("f\"[^\"]+\"",parser.expDef[i])
                if errorPrint:
                    size = len(errorPrint.group(0)) + 1
                    flex.write("\n  print("+errorPrint.group(0)+")")
                    parser.expDef[i] = parser.expDef[i][size:]
                    sizeExp -= size
                else:
                    statement = re.search("[^,]+",parser.expDef[i])
                    size = len(statement.group(0))  + 1
                    flex.write("\n  "+statement.group(0))
                    parser.expDef[i] = parser.expDef[i][size:]
                    sizeExp -= size
            flex.write("\n")

#-----------------------------------------PRECEDENCE----------------------------------------------

def writePrecedence(precedence):
    fyacc.write("precedence = "+precedence + "\n")

#-------------------------------------------GRAMMARYACC----------------------------------------------
def writeGram(parser):
    contador = 0
    expAnt = ""

    parser.expGram.reverse()
    parser.funcGram.reverse()

    for i in range(0,len(parser.expGram)):
        div = parser.expGram[i].split(":")
        if div[0].strip(" ") == expAnt:
            contador += 1
        else:
            contador = 0
            expAnt = div[0].strip(" ")
        funFinal = re.sub("[\s\{\}]","",parser.funcGram[i])

        fyacc.write("def p_" + expAnt + "_" + str(contador)+ "(p):\n")
        fyacc.write("\t\"" + parser.expGram[i] +"\"\n")        
        fyacc.write("\t" + funFinal +"\n")       

def writeValues(initVal):

    initVal.reverse()

    for i in range(0,len(initVal)):
        fyacc.write(initVal[i])

#-------------------------------------------GRAMMAR----------------------------------------------

def p_GRAMMATICA(p):
    "Z : GRAMMAR"

    writeLiterals(parser.literals)
    writeIgnore(parser.ignore)
    writeTokens(parser.tokens)    
    writeExpDefs(parser)
    writePrecedence(parser.precedence)
    writeValues(parser.initVal)
    writeGram(parser)
    
            
def p_GRAMMAR_lex(p):
    "GRAMMAR : GRAMMAR LEX"

def p_GRAMMAR_yacc(p):
    "GRAMMAR : GRAMMAR YACC"

def p_GRAMMAR_python(p):
    "GRAMMAR : GRAMMAR python"

def p_GRAMMAR_empty(p):
    "GRAMMAR : "



#-------------------------------------------LEX----------------------------------------------

def p_LEX(p):
    "LEX : lex LEXES "
    flex.write("import ply.lex as lex\n")
    flex.write("lexer = lex.lex()\n")

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
    parser.ignore = p[3]

#--------------------------------------------ExpDefs-----------------------------------------------

def p_LEXES_EXPDEFS(p):
    "LEXES : er LISTEXPDEFS LEXES"

def p_LEXES_LISTEXPDEFS(p):
    "LISTEXPDEFS : expReg expDef LISTEXPDEFS"
    parser.expReg.append(p[1])
    parser.expDef.append(p[2])

def p_LEXES_LISTEXPDEFS_empty(p):
    "LISTEXPDEFS : "


#--------------------------------------------EMPTY LEX-----------------------------------------------


def p_LEXES_EMPTY(p):
    "LEXES : "


#--------------------------------------------YACC-----------------------------------------------
def p_YACC(p):
    "YACC : yacc YACCS"
    fyacc.write("import ply.yacc as yacc\n")
    fyacc.write("parser = yacc.yacc()\n")

#-------------------------------------------PRECEDENCE----------------------------------------------

def p_YACCS_PREC(p):
    "YACCS : precedence equal listprecedence YACCS"
    parser.precedence = p[3]

#-------------------------------------------INITVALUES----------------------------------------------

def p_YACCS_initParserVal(p):
    "YACCS : initParserVal LISTVALUES YACCS"

def p_YACCS_valores(p):
    "LISTVALUES : parserVal LISTVALUES"
    parser.initVal.append(p[1])

def p_YACCS_empty(p):
    "LISTVALUES : endParserVal"    
#-------------------------------------------GRAMMAR----------------------------------------------

def p_YACCS_GRAMMAR(p):
    "YACCS : grammar LISTGRAM YACCS"

def p_YACCS_LISTGRAM(p):
    "LISTGRAM : grammarDef funcGrammar LISTGRAM"
    parser.expGram.append(p[1])
    parser.funcGram.append(p[2])

def p_YACCS_LISTGRAM_empty(p):
    "LISTGRAM : "
#--------------------------------------------EMPTY YACC-----------------------------------------------

def p_YACC_EMPTY(p):
    "YACCS : "

def p_error(p):
    print('Erro sintatico: ', p)
    parser.sucess = False


parser = yacc.yacc()
parser.tokens = []
parser.literals = ""
parser.ignore = ""
parser.expReg = []
parser.expDef = []
parser.precedence = ""
parser.initVal = []
parser.expGram = []
parser.funcGram = []

parser.parse(sys.stdin.read())