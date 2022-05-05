
literals = ",+/"
t_ignore = " \n\t"
tokens = ['NUMBER','VAR']

def t_error(t):
  print("Illegal character '"+t.value[0]+"', ["+t.lexer.lineno+"]")

def t_NUMBER(t):
  r'\d+(\.\d+)?'
  return t

def t_VAR(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  return t
