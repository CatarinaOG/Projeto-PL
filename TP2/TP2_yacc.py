#!/usr/bin/env python

from io import TextIOWrapper
from posixpath import split
import ply.yacc as yacc
import re
from TP2_lex import tokens
import sys
import os

flex : TextIOWrapper = None
fyacc : TextIOWrapper = None


#-------------------------------------------LITERALS----------------------------------------------

def writeLiterals(literals):
    if literals:
        flex.write("\nliterals = "+literals)

#-------------------------------------------IGNORE----------------------------------------------

def writeIgnore(ignore):
    if ignore:
        flex.write("\nt_ignore = "+ignore)

#-------------------------------------------TOKENS----------------------------------------------

#função que pegva no elemento do return entre ' que é o token associado
def tokenNameFunc(expDef):
    name = re.search("\'.+\'",expDef)
    return name.group(0).strip("\'")


def writeTokens(tokens, comment):
    if tokens:
        flex.write("\ntokens = [\'"+tokens[0]+"\'")
        for token in tokens[1:]:
            flex.write(",\'"+token+"\'")
        if comment:
            flex.write("]\t#"+comment+"\n")
        else:
            flex.write("]\n")

#remove os parenteses desnecessário por causa do split
def removeLastPar(result):
    i = len(result) -1
    s = list(result)
    while i > 0:
        if s[i] == ')':
            s[i] = ''
            s[i+1] = ''
            break
        i = i -1
    return "".join(s)

#-------------------------------------------EXP DEF----------------------------------------------

def writeExpDefs(parser):

    if parser.expDef and parser.expReg:
        nrExp = len(parser.expDef)

        parser.expDef.reverse()
        parser.expReg.reverse()

        for i in range(0,nrExp):
            if parser.expReg[i] != '.':
                resultado = parser.expDef[i].split(",")
                tokenName = tokenNameFunc(resultado[0])
                if tokenName in parser.tokens:
                    flex.write("\ndef t_" + tokenName + "(t):")
                    flex.write("\n\tr\'" + parser.expReg[i] + "\'")
                    flex.write("\n\tt.value = " + removeLastPar(resultado[1]))
                    flex.write("\n\treturn t\n")
                else:
                    print("Token inválido")
            else:
                flex.write("\ndef t_error(t):")

                parser.expDef[i] = parser.expDef[i][7:]
                print(parser.expDef[i])
                aux = parser.expDef[i].split(";")
                sizeExp = len(aux[0])
                while sizeExp > 0:
                    errorPrint = re.match("f\"[^\"]+\"",aux[0])
                    if errorPrint:
                        size = len(errorPrint.group(0)) + 1
                        flex.write("\n\tprint("+errorPrint.group(0)+")")
                        aux[0] = aux[0][size:]
                        sizeExp -= size
                    else:
                        statement = re.search("[^,]+",aux[0])[0]
                        size = len(statement)  + 1
                        flex.write("\n\t"+statement)
                        aux[0] = aux[0][size:]
                        sizeExp -= size
                if len(aux) > 1:
                    flex.write(aux[1])
                flex.write("\n")

#-----------------------------------------PRECEDENCE----------------------------------------------

def writePrecedence(precedence):
    if precedence:
        fyacc.write("\nprecedence = "+precedence + "\n")

#-------------------------------------------GRAMMARYACC----------------------------------------------

def writeGram(parser):


    if parser.funcGram and parser.expGram:
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
            funFinal = re.sub("[ \{\}]","",parser.funcGram[i])
            fyacc.write("\ndef p_" + expAnt + "_" + str(contador)+ "(p):\n")
            fyacc.write("\t\"" + parser.expGram[i] +"\"\n")
            fyacc.write("\t" + funFinal +"\n")

def writeValues(initVal):

    if initVal:
        initVal.reverse()

        for i in range(0,len(initVal)):
            fyacc.write(initVal[i])


#-------------------------------------------PYTHONFUNCS----------------------------------------------

def writePythonFuncs(funcs):

    funcs.reverse()

    for i in range(0,len(funcs)):
        if re.match(r'def',funcs[i]):
            fyacc.write("\n\n"+funcs[i])
        else:
            fyacc.write(funcs[i])

#-------------------------------------------PYTHONOTHERS----------------------------------------------

def writePythonOther(others):

    others.reverse()

    for i in range(0,len(others)):
        if re.search(r'yacc\(\)',others[i]):
            fyacc.write(re.sub("yacc\(\)","yacc.yacc()",others[i]))
        else:
            fyacc.write(others[i])

#-------------------------------------------GRAMMAR----------------------------------------------

def p_GRAMMATICA(p):
    "Z : GRAMMAR"

    writeLiterals(parser.literals)
    writeIgnore(parser.ignore)
    writeTokens(parser.tokens,parser.commentsToken)
    writeExpDefs(parser)
    flex.write("\nlexer = lex.lex()")
    writePrecedence(parser.precedence)
    writeValues(parser.initVal)
    writeGram(parser)
    writePythonFuncs(parser.pythonFuncs)
    writePythonOther(parser.pythonOthers)

def p_GRAMMAR_lex(p):
    "GRAMMAR : GRAMMAR LEX"

def p_GRAMMAR_yacc(p):
    "GRAMMAR : GRAMMAR YACC"

def p_GRAMMAR_python(p):
    "GRAMMAR : GRAMMAR PYTHON"

def p_GRAMMAR_empty(p):
    "GRAMMAR : "



#-------------------------------------------LEX----------------------------------------------

def p_LEX(p):
    "LEX : lex LEXES "
    flex.write("import ply.lex as lex\n")

#-------------------------------------------LITERALS----------------------------------------------

def p_LEXES_LITERALSCOM(p):
    "LEXES : literals equal listliterals comment commentEnd LEXES"
    parser.literals = p[3]+"\t#"+p[5]
    fyacc.write("from lex import literals\n")

def p_LEXES_LITERALS(p):
    "LEXES : literals equal listliterals LEXES"
    parser.literals = p[3]
    fyacc.write("from lex import literals\n")


#-------------------------------------------TOKENS----------------------------------------------
def p_LEXES_TOKENSCOM(p):
    "LEXES : tokens equal oBracket LISTTOKENS cBracket comment commentEnd LEXES "
    fyacc.write("from lex import tokens\n")
    parser.commentsToken = p[7]

def p_LEXES_TOKENS(p):
    "LEXES : tokens equal oBracket LISTTOKENS cBracket LEXES "
    fyacc.write("from lex import tokens\n")

def p_LISTTOKENS(p):
    "LISTTOKENS : prime token prime CONTLISTTOKENS"
    parser.tokens.append(p[2])

def p_CONTLISTTOKENS(p):
    "CONTLISTTOKENS : comma prime token prime CONTLISTTOKENS "
    parser.tokens.append(p[3])

def p_CONTLISTTOKENS_EMPTY(p):
    "CONTLISTTOKENS : "


#-------------------------------------------IGNORE----------------------------------------------

def p_LEXES_IGNORECOM(p):
    "LEXES : ignor equal listignore comment commentEnd LEXES"
    parser.ignore = p[3] + "\t#" + p[5]

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

def p_LEXES_LISTEXPDEFSCOM(p):
    "LISTEXPDEFS : expReg expDef comment commentEnd LISTEXPDEFS"
    parser.expReg.append(p[1])
    parser.expDef.append(p[2] + "\t#" + p[4])

def p_LEXES_LISTEXPDEFS_empty(p):
    "LISTEXPDEFS : "


#--------------------------------------------EMPTY LEX-----------------------------------------------


def p_LEXES_EMPTY(p):
    "LEXES : "


#--------------------------------------------YACC-----------------------------------------------
def p_YACC(p):
    "YACC : yacc YACCS"
    fyacc.write("import ply.yacc as yacc\n")

#-------------------------------------------PRECEDENCE----------------------------------------------

def p_YACCS_PREC(p):
    "YACCS : precedence equal listprecedence YACCS"
    parser.precedence = p[3]

def p_YACCS_PRECCOM(p):
    "YACCS : precedence equal listprecedence comment commentEnd YACCS"
    parser.precedence = p[3] + "\t#" + p[5]

#-------------------------------------------INITVALUES----------------------------------------------

def p_YACCS_initParserVal(p):
    "YACCS : initParserVal LISTVALUES YACCS"

def p_YACCS_valores(p):
    "LISTVALUES : parserVal LISTVALUES"
    parser.initVal.append(p[1])

def p_YACCS_valoresCOM(p):
    "LISTVALUES : parserVal comment commentEnd LISTVALUES"
    parser.initVal.append(p[1] + "\t#" + p[3])

def p_YACCS_empty(p):
    "LISTVALUES : endParserVal"

#-------------------------------------------GRAMMAR----------------------------------------------

def p_YACCS_GRAMMAR(p):
    "YACCS : grammar LISTGRAM YACCS"

def p_YACCS_LISTGRAMCOM(p):
    "LISTGRAM : grammarDef funcGrammar comment commentEnd LISTGRAM"
    parser.expGram.append(p[1])
    parser.funcGram.append(p[2] +"\t#" + p[4])

def p_YACCS_LISTGRAM(p):
    "LISTGRAM : grammarDef funcGrammar LISTGRAM"
    parser.expGram.append(p[1])
    parser.funcGram.append(p[2])

def p_YACCS_LISTGRAM_empty(p):
    "LISTGRAM : "
#--------------------------------------------EMPTY YACC-----------------------------------------------

def p_YACC_EMPTY(p):
    "YACCS : "

#--------------------------------------------PYTHON-----------------------------------------------

def p_PYTHON(p):
    "PYTHON : python PYTHONS"

def p_PYTHONS(p):
    "PYTHONS : LISTFUNCS LISTOTHER"

def p_PYTHON_ListFuncs(p):
    "LISTFUNCS : funcPython LISTFUNCS"
    parser.pythonFuncs.append(p[1])

def p_PYTHON_ListFuncsEmpty(p):
    "LISTFUNCS : "

def p_PYTHON_ListOther(p):
    "LISTOTHER : otherPython LISTOTHER"
    parser.pythonOthers.append(p[1])

def p_PYTHON_ListOtherEmpty(p):
    "LISTOTHER : "



def p_error(p):
    print('Erro sintatico: ', p)
    parser.sucess = False


parser = None

def main():

    global flex
    global fyacc

    dirName = "out"
    if not os.path.exists(dirName):
        os.mkdir(dirName)

    fyacc = open(dirName + "/yacc.py", "w")
    flex = open(dirName + "/lex.py", "w")


    global parser
    parser = yacc.yacc()

    parser.tokens = []
    parser.commentsToken = ""
    parser.literals = ""
    parser.ignore = ""
    parser.expReg = []
    parser.expDef = []
    parser.precedence = ""
    parser.initVal = []
    parser.expGram = []
    parser.funcGram = []
    parser.pythonFuncs = []
    parser.pythonOthers = []

    parser.parse(sys.stdin.read())

    flex.close()
    fyacc.close()



if __name__ == '__main__':
    main()