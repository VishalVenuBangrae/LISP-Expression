import ply.lex as lex

reserved = { 'car': 'CAR', 'cdr': 'CDR', 'cons': 'CONS', 'let': 'LET' }

tokens = ['OP','LPAREN','RPAREN','NUMBER','VAR','SEMI'] + list(reserved.values())

t_OP = r'\+|-|\*|\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_CAR = r'[Cc][Aa][Rr]'
t_CDR = r'[Cc][Dd][Rr]'
t_CONS = r'[Cc][Oo][Nn][Ss]'
t_LET = r'[Ll][Ee][Tt]'
t_SEMI = r';'

def t_NUMBER(t):
  r'[0-9]+(\.[0-9]*)?'
  t.value = float(t.value)
  return t

def t_VAR(t):
  r'[a-zA-Z][a-zA-Z0-9]*'
  t.type = reserved.get(t.value.lower(),'VAR')
  return t

# Ignored characters
t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'

def t_error(t):
  print("\nLEXER ERROR: Illegal character '%s'\n" % t.value[0])
  raise Exception('LEXER ERROR')

lexer = lex.lex()
## Test it out
#data = '''
##(* (+ 1 2) (/ 8 4))
#(let ((x 2)(y 4)) (+ x y));
#'''
#
## Give the lexer some input
#lexer.input(data)
#
## Tokenize
#while True:
#    tok = lexer.token()
#    if not tok:
#        break      # No more input
#    print(tok)