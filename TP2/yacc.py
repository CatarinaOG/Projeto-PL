import ply.yacc as yacc
parser = yacc.yacc()
precedence = [
    ('left','+','-'),
    ('left','*','/'),
    ('right','UMINUS'),
]
ts = {}
a=3
def p_stat_0(p):
	"stat : VAR '=' exp	"
	ts[p[1]]=p[3]
def p_stat_1(p):
	"stat : exp	"
	print(p[1])
def p_exp_0(p):
	"exp : exp '+' exp	"
	p[0]=p[1]+p[3]
def p_exp_1(p):
	"exp : exp '-' exp	"
	p[0]=p[1]-p[3]
def p_exp_2(p):
	"exp : exp '*' exp	"
	p[0]=p[1]*p[3]
def p_exp_3(p):
	"exp : exp '/' exp	"
	p[0]=p[1]/p[3]
def p_exp_4(p):
	"exp : '-' exp	"
	p[0]=-p[2]
def p_exp_5(p):
	"exp : '(' exp ')'	"
	p[0]=p[2]
def p_exp_6(p):
	"exp : NUMBER	"
	p[0]=p[1]
def p_exp_7(p):
	"exp : VAR	"
	p[0]=getval(p[1]) 
