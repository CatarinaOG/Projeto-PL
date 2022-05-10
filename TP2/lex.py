import ply.lex as lex
lexer = lex.lex()

literals = ",+/"
t_ignore = " \n\t"
tokens = ['NUMBER','VAR']

def t_VAR(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  return('VAR', t.value)	

def t_NUMBER(t):
  r'\d+(\.\d+)?'
  return('NUMBER', float(t.value))

def t_error(t):
  print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
  t.lexer.skip(1)
  print(f"hello")
import ply.lex as lex
lexer = lex.lex()

literals = ",+/"
t_ignore = " \n\t"
tokens = ['NUMBER','VAR']

def t_VAR(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  return('VAR', t.value)	

def t_NUMBER(t):
  r'\d+(\.\d+)?'
  return('NUMBER', float(t.value))

def t_error(t):
  print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
  t.lexer.skip(1)
  print(f"hello")
import ply.lex as lex
lexer = lex.lex()

literals = ",+/"
t_ignore = " \n\t"
tokens = ['NUMBER','VAR']

def t_VAR(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  return('VAR', t.value)	

def t_NUMBER(t):
  r'\d+(\.\d+)?'
  return('NUMBER', float(t.value))

def t_error(t):
  print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
  t.lexer.skip(1)
  print(f"hello")
import ply.lex as lex
lexer = lex.lex()

literals = ",+/"
t_ignore = " \n\t"
tokens = ['NUMBER','VAR']

def t_VAR(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  return('VAR', t.value)	

def t_NUMBER(t):
  r'\d+(\.\d+)?'
  return('NUMBER', float(t.value))

def t_error(t):
  print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
  t.lexer.skip(1)
  print(f"hello")
import ply.lex as lex
lexer = lex.lex()

literals = ",+/"
t_ignore = " \n\t"
tokens = ['NUMBER','VAR']

def t_VAR(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  return('VAR', t.value)	

def t_NUMBER(t):
  r'\d+(\.\d+)?'
  return('NUMBER', float(t.value))

def t_error(t):
  print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
  t.lexer.skip(1)
  print(f"hello")
import ply.lex as lex
lexer = lex.lex()

literals = ",+/"
t_ignore = " \n\t"
tokens = ['NUMBER','VAR']

def t_VAR(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  return('VAR', t.value)	

def t_NUMBER(t):
  r'\d+(\.\d+)?'
  return('NUMBER', float(t.value))

def t_error(t):
  print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
  t.lexer.skip(1)
  print(f"hello")
import ply.lex as lex
lexer = lex.lex()

literals = ",+/"
t_ignore = " \n\t"
tokens = ['NUMBER','VAR']

def t_VAR(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  return('VAR', t.value)	

def t_NUMBER(t):
  r'\d+(\.\d+)?'
  return('NUMBER', float(t.value))

def t_error(t):
  print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
  t.lexer.skip(1)
  print(f"hello")
