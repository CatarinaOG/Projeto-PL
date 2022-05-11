import ply.lex as lex

literals = "+-/*=()"	#isto sao literals
t_ignore = " \n\t"	#isto sao ignores
tokens = ['NUMBER','VAR']	#mais um comentario pros tokens

def t_VAR(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.value =  t.value	#oiiiiii
	return t

def t_NUMBER(t):
	r'\d+(\.\d+)?'
	t.value =  float(t.value)	#ppppppp
	return t

def t_error(t):
	print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
	t.lexer.skip(1)
	print(f"hello")	#oqoqoqoqoqoq

lexer = lex.lex()