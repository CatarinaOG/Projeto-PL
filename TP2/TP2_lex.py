import ply.lex as lex

tokens = ['lex','yacc','python','literals','listliterals','equal','colon','comma',
        'quote','token','tokens','oBracket','cBracket','ignor','listignore','precedence',
        'listprecedence','prime','er','expReg','expDef','initParserVal','parserVal','endParserVal','grammar','grammarDef','funcGrammar'
        ,'funcPython','otherPython']


states = ( 
    ('LEX','exclusive'),
    ('YACC','exclusive'),
    ('PYTHON','exclusive'),
    ('COMMENT','exclusive'),
    ('IGNORE','exclusive'),
    ('TOKENDEF','exclusive'),
    ('GRAMMAR','exclusive'),
    ('PARSEVALUES','exclusive'),
    
)

t_ANY_ignore = " \t\r\n"
t_IGNORE_ignore =  "\t\r\n"
t_TOKENDEF_ignore =  "\t\r\n"
t_YACC_ignore = " \t\r\n"
t_GRAMMAR_ignore =  " \t\r\n"
t_PARSEVALUES_ignore =  " \t\r\n"
t_PYTHON_ignore =  " \r\n"
#-------------------------------------------LEX----------------------------------------------

def t_ANY_lex(t):
    r'%%LEX'
    t.lexer.begin("LEX")
    return t


#-------------------------------------------YACC----------------------------------------------

def t_ANY_yacc(t):
    r'%%YACC'
    t.lexer.begin("YACC")
    return t

#-------------------------------------------PYTHON----------------------------------------------

def t_ANY_python(t):
    r'%%'
    t.lexer.begin("PYTHON")
    return t

#-------------------------------------------COMMENT----------------------------------------------
"""
def t_ANY_comment(t):
    r'\#'
    t.lexer.begin("COMMENT")
    return t
def t_COMMENT_end(t):
    r'\#'
    t.lexer.begin("INITIAL")
    return t
"""

#-------------------------------------------LITERALS----------------------------------------------

def t_LEX_literals(t):
    r'%literals'
    return t

def t_ANY_equal(t):
    r'='
    return t

def t_LEX_listliterals(t):
    r'\"[^a-zA-Z0-9]+\"'
    return t


#-------------------------------------------TOKENS----------------------------------------------

def t_LEX_tokens(t):
    r'%tokens'
    return t


def t_LEX_token(t):
    r'[a-zA-Z]+'
    return t

#-------------------------------------------IGNORE----------------------------------------------

def t_LEX_ignor(t):
    r'%ignore'
    t.lexer.begin("IGNORE")
    return t


def t_IGNORE_listignore(t):
    r'\".+\"'
    t.lexer.begin("LEX")
    return t

#-------------------------------------------RegularExpression----------------------------------------------


def t_LEX_er(t):
    r'%er\r\n'
    t.lexer.begin("TOKENDEF")
    return t

def t_TOKENDEF_expReg(t):
    r'[^\s]+'
    return t

def t_TOKENDEF_expDef(t):
    r'[^\n]+'
    return t

#-------------------------------------------PRECEDENCE----------------------------------------------

def t_YACC_precedence(t):
    r'%precedence'
    return t

def t_YACC_listprecedence(t):
    r'\[[^\]]+\]'
    return t

#-------------------------------------------DECLARATIONS----------------------------------------------

def t_YACC_initParserVal(t):
    r'%symboltable'
    t.lexer.begin("PARSEVALUES")
    return t
    
def t_PARSEVALUES_endParserVal(t):
    r'%symboltablend'
    t.lexer.begin("YACC")
    return t

def t_PARSEVALUES_parserVal(t):
    r'[^\n]+\n'
    return t

#-------------------------------------------Grammar----------------------------------------------

def t_YACC_grammar(t):
    r'%grammar'
    t.lexer.begin("GRAMMAR")
    return t

def t_GRAMMAR_grammarDef(t):
    r'[^\t\n]+\t'
    return t

def t_GRAMMAR_funcGrammar(t):
    r'[^\n]+\n'
    return t


#-------------------------------------------PYTHON----------------------------------------------

def t_PYTHON_funcPython(t):
    r'[def|\s]+.+'
    return t

def t_PYTHON_otherPython(t):
    r'.+'
    return t

#-------------------------------------------OURS_LITERALS----------------------------------------------


def t_ANY_colon(t):
    r':'
    return t

def t_ANY_comma(t):
    r','
    return t

def t_ANY_prime(t):
    r'\''
    return t

def t_LEX_cBracket(t):
    r'\]'
    return t

def t_LEX_oBracket(t):
    r'\['
    return t

#-------------------------------------------funcoes----------------------------------------------

def t_ANY_error(t):
    t.lexer.skip(1)
    return t


lexer = lex.lex()
""""
import sys
lexer.input(sys.stdin.read())
for tok in lexer:
    print(tok)
"""