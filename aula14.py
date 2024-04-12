# Outras formas de formatação

a = 'A'

b = 'B'

c = 1.1
# format sempre usa a orde, mas numerando ele, tira essa obrigação da ordem
# Sempre começa pelo (0)
string = 'a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c)

print(formato)
