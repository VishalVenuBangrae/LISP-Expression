import ply.yacc as yacc
from LispLexer import tokens


def p_start_1(p):
    'start : list SEMI'
    p[0] = ['LIST', p[1]]


def p_start_2(p):
    'start : num SEMI'
    p[0] = ['NUM', p[1]]


def p_num_1(p):
    'num : NUMBER'
    p[0] = ['num', p[1]]


def p_num_2(p):
    'num : VAR'
    p[0] = ['var', p[1]]


def p_num_3(p):
    'num : LPAREN OP num num RPAREN'
    p[0] = [p[2], p[3], p[4]]


def p_num_4(p):
    'num : LPAREN CAR list RPAREN'
    p[0] = ['car', p[3]]


def p_num_5(p):
    'num : LPAREN LET LPAREN vars RPAREN num RPAREN'
    p[0] = ['let', p[4], p[6]]


def p_list_1(p):
    'list : LPAREN seq RPAREN'
    p[0] = p[2]


def p_list_2(p):
    'list : LPAREN CDR list RPAREN'
    p[0] = ['cdr', p[3]]


def p_list_3(p):
    'list : LPAREN CONS num list RPAREN'
    p[0] = [p[3], p[4]]


def p_seq_1(p):
    'seq :'
    p[0] = []


def p_seq_2(p):
    'seq : num seq'  # right recursion on purpose; to enable LISP Lists!
    p[0] = [p[1], p[2]]


def p_vars_1(p):
    'vars : LPAREN VAR num RPAREN'
    p[0] = [[p[2], p[3]]]


def p_vars_2(p):
    'vars : vars LPAREN VAR num RPAREN'
    p[0] = p[1] + [[p[3], p[4]]]


def p_error(p):
    print("\nSYNTAX ERROR\n")


parser = yacc.yacc()
