import ply.lex as lex

tokens = ['lex','yacc','func','literals','listliterals','equal','colon','comma',
        'quote','token','tokens','oBracket','cBracket','ignor','listignore','precedence','listprecedence']

t_ignore = " \t\n"
t_ignore_COMMENT = r'\#.*'


#-------------------------------------------LEX----------------------------------------------

def t_lex(t):
    r'%%\s*LEX'
    return t

#-------------------------------------------YACC----------------------------------------------

def t_yacc(t):
    r'%%\s*YACC'
    return t

#-------------------------------------------FUNC----------------------------------------------

def t_func(t):
    r'%%'
    return t


#-------------------------------------------LITERALS----------------------------------------------

def t_literals(t):
    r'%literals'
    return t

def t_equal(t):
    r'='
    return t

def t_listliterals(t):
    r'\"[^a-zA-Z0-9]+\"'
    return t

#-------------------------------------------TOKENS----------------------------------------------

def t_tokens(t):
    r'%tokens'
    return t

def t_cBracket(t):
    r'\]'
    return t

def t_oBracket(t):
    r'\['
    return t

def t_token(t):
    r'(\'[a-zA-Z]+\')'
    return t

#-------------------------------------------IGNORE----------------------------------------------

def t_ignor(t):
    r'%ignore'
    return t

def t_listignore(t):
    r'\".+\"'
    return t

#-------------------------------------------PRECEDENCE----------------------------------------------
def t_precedence(t):
    r'%precedence'
    return t

def t_listprecedence(t):
    r'\(.+?\)'
    return t

#-------------------------------------------OURS_LITERALS----------------------------------------------


def t_colon(t):
    r':'
    return t

def t_comma(t):
    r','
    return t


#-------------------------------------------funcoes----------------------------------------------

def t_error(t):
    print("Carater ilegal: ",t.value[0])

lexer = lex.lex()
