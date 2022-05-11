from lex import tokens
from lex import literals
import ply.yacc as yacc
precedence = [
    ('left','+','-'),
    ('left','*','/'),
    ('right','UMINUS'),
]	#pooosososo
ts = {}	##oorororororroor
a = 3	##papaasllslsalça

def p_stat_0(p):
	"stat : VAR '=' exp	"
	ts[p[1]]=p[3]

def p_stat_1(p):
	"stat : exp	"
	print(p[1])	#opepepepepepe

def p_exp_0(p):
	"exp : exp '+' exp	"
	p[0]=p[1]+p[3]

def p_exp_1(p):
	"exp : exp '-' exp	"
	p[0]=p[1]-p[3]

def p_exp_2(p):
	"exp : exp '*' exp	"
	p[0]=p[1]*p[3]	#portoooooooooo

def p_exp_3(p):
	"exp : exp '/' exp	"
	p[0]=p[1]/p[3]

def p_exp_4(p):
	"exp : '-' exp %prec UMINUS	"
	p[0]=-p[2]	#oizes

def p_exp_5(p):
	"exp : '(' exp ')' 	"
	p[0]=p[2]

def p_exp_6(p):
	"exp : NUMBER	"
	p[0]=p[1]

def p_exp_7(p):
	"exp : VAR	"
	p[0]=getval(p[1])


def p_error(t):         ## HELLO	print(f"Syntax error at '{t.value}', [{t.lexer.lineno}]")

def getval(n):	if n not in ts: print(f"Undefined name '{n}'")	return ts.get(n,0)y=yacc.yacc()	##papapsplsy.parse("3+4*7")	#palslalspas