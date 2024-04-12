# Interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'gavioes'
preco = 100.95897643
variavel = '%s, o preço total foi R$%f' % (nome, preco) # pode usar o 2.f para diminuir as casas do numero
print(variavel)
print('O hexadecimal de %d é %04x' % (15, 15)) #voce pode colocar qualquer letra o importante é definir o valor no ()
