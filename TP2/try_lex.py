import ply.lex as lex

literals = "=\'\""
tokens = ['lex','yacc','func','num','literals','literal']


t_lex = r'%%\sLEX'
t_yacc = r'%%\sYACC'
t_func = r'%%'
t_literals = r'%literals'
t_literal = r'[^a-zA-Z0-9]'

def t_num(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t\n "

def t_error(t):
    print("Carater ilegal: ",t.value[0])

lexer = lex.lex() 