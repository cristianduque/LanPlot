import ply.lex as lex
# import FourierTransform
import numpy as np
from FourierTransform import FourierTransform

# list of tokens names

tokens = ('PLOT',
          'FOURIERTRANSFORM',
          'NUMBER',
          'PLUS',
          'MINUS',
          'TIMES',
          'DIVIDE',
          'LPARENT',
          'RPARENT',
          'EXPONENT',
          'EQUALS',
          'EXPRNAME',
          'COMMA',
          'SIN',
          'COS',
          'EXP',
          'PULSE',
          'PI',
          'VART',
        )

# reserved words
reserved = {
            'plot':'PLOT',
            'fouriertransform': 'FOURIERTRANSFORM'
}

functions = {
            'cos': 'COS',
            'sin': 'SIN',
            'exp': 'EXP',
            'pi' : 'PI'
}

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPARENT  = r'\('
t_RPARENT  = r'\)'
t_EXPONENT = r'\^'
t_PLOT = r'(?i)plot'
t_COS = r'(?i)cos'
t_SIN = r'(?i)sin'
t_EXP = r'(?i)exp'
t_PI = r'(?i)pi'
t_FOURIERTRANSFORM = r'(?i)fouriertransform'
t_PULSE = r'(?i)pulse'
t_EQUALS = r'\='
t_COMMA = r'\,'
t_VART = r't'

# A regular expression rule with some action code
def t_NUMBER(t):
    #r'-?\d+'
    r'\d+'
    t.value = int(t.value)
    return t

def t_EXPRNAME(t):
    r'(([A-Za-z]+[0-9]+)|([A-Za-z][A-Za-z]+[0-9]*))+'
    if t.value in 'plot':
        t.type = reserved.get(t.value,'ID')
    if t.value in 'fouriertransform':
        t.type = reserved.get(t.value,'ID')
    if t.value in 'sin':
        t.type = functions.get(t.value,'ID')
    if t.value in 'cos':
        t.type = functions.get(t.value,'ID')
    if t.value in 'exp':
        t.type = functions.get(t.value,'ID')
    if t.value in 'pi':
        t.type = functions.get(t.value,'ID')
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

# Ignore strings starting with # (comments)
t_ignore_COMMENT = r'\#.*'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
# data = '''cos(2*pi*50*t)'''

# Give the lexer some input
# lexer.input(data)

def printok():
    while True:
        tok = lexer.token()
        if not tok: break
        print(tok.type, tok.value)

# Yacc test

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
names = {}

#############LangFunctions###############

def p_langfunctions1(p):
    'langfunction : plot'
    p[0] = str(p[1])

def p_langfunctions1(p):
    'langfunction : function'
    p[0] = str(p[1])

def p_langfunctions2(p):
    'langfunction : exprname'
    p[0] = str(p[1])

#############FOURIER TRANSFORM###############
def p_fouriertransform(p):
    'fouriertransform : expression COMMA factor'
    p[0] = str(p[1]) + str(p[3])


#############EXPRESSION NAME###############   #OK
def p_exprname(p):
    'exprname : EXPRNAME'
    p[0] = str(p[1])

# def p_exprname1(p):
#     'exprname : EXPRNAME EQUALS function'
#     names[p[1]] = p[3]
#     p[0] = p[1]

def p_exprname2(p):
    'exprname : EXPRNAME EQUALS expression COMMA expression'
    names[p[1]] = str(p[3] + ',' + p[5])
    p[0] = p[1]

def p_exprname3(p):
    'exprname : EXPRNAME EQUALS EXPRNAME'
    names[p[1]] = names[p[3]]
    p[0] = p[1]

#############FUNCTION###############
def p_function(p):
    'function : PLOT FOURIERTRANSFORM expression COMMA expression'
    pol = FourierTransform(p[3], int(p[5])).compute()
    #print pol
    p[0] = pol

def p_function7(p):
    'function : PLOT FOURIERTRANSFORM exprname'
    equation, number_pointsamples = names[p[3]].split(',')
    pol = FourierTransform(equation, int(number_pointsamples)).compute()
    # print pol
    p[0] = pol

def p_function6(p):
    'function : PLOT FOURIERTRANSFORM LPARENT expression RPARENT'
    p[0] = str(p[1]) + '(' + str(p[3]) + ')'
    pol = FourierTransform(p[3]).compute()
    #print pol
    p[0] = pol



############EXPRESSION###############   #OK
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = str(p[1]) + '+' + str(p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = str(p[1]) + '-' + str(p[3])

def p_expression_cos(p):
    'expression : COS LPARENT expression RPARENT'
    p[0] = p[1] + '(' + p[3] + ')'

def p_expression_sin(p):
    'expression : SIN LPARENT expression RPARENT'
    p[0] = p[1](p[3])

def p_expression_exp(p):
    'expression : EXP LPARENT expression RPARENT'
    p[0] = p[1](p[3])

def p_expression_cos_amplitude(p):
    'expression : term COS LPARENT expression RPARENT'
    p[0] = p[1]*(p[2](p[4]))

def p_expression_sin_amplitude(p):
    'expression : term SIN LPARENT expression RPARENT'
    p[0] = p[1]*(p[2](p[4]))

def p_expression_exp_amplitude(p):
    'expression : term EXP LPARENT expression RPARENT'
    p[0] = p[1]*(p[2](p[4]))


def p_expression_times(p):
    'expression : expression TIMES term'
    p[0] = str(p[1]) + '*' + str(p[3])

def p_expression_divide(p):
    'expression : expression DIVIDE term'
    p[0] = str(p[1]) + '/' + str(p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = str(p[1])

##############TERM##################    #OK
def p_term_times(p):
    'term : factor variable'
    p[0] = str(p[1]) + str(p[2])

def p_term_var_exp(p):
    'term : variable EXPONENT factor'
    p[0] = str(p[1]) + '^' + str(p[3])

def p_term_var(p):
    'term : variable'
    p[0] = str(p[1])

def p_term_fac(p):
    'term : factor'
    p[0] = str(p[1])

##############FACTOR################    #OK
def p_factor_num(p):
    'factor : NUMBER'
    p[0] = str(p[1])

def p_factor_pi(p):
    'factor : PI'
    p[0] = str(p[1])

#############VARIABLE###############
def p_variable_t(p):
    'variable : VART'
    p[0] = str(p[1])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('(LanPlot) > ')   # use input() on Python 3
    except EOFError:
        break
    result = parser.parse(s)
    print(result)