# Formatação básica de strings
# s - string
# d - int
# f - float 
# . <numero de digitos> f
# x ou X - Hexadecimal
# (Caractere) (><^) (quantidade)
# > - esquerda
# < - direita 
# ^ - centro
# = - Força o número a aparecer antes dos zeros
# Sinal - + ou -
# Ex.: 0>-100, 1.f
# Conversion flags - !r !s !a

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')  # executando ele fica com espaço de 10 para esquerda
print(f'{variavel: <10}')  # executando ele fica com espaço de 10 para direita
print(f'{variavel: ^10}')  # executando ele fica centralizado no meio
print(f'{1000.921831939:+,.1f}')   # + obriga a aparecer o numero positivo tambem
print('O hexadecimal de 1500 é {1500:08X}')
prin(f'{variavel!r}')  # outros métodos 