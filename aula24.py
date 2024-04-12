# Operadores in e not in
# Strings são interáveis ( pode navegar intem por intem)
# 0 1 2 3 4 5
# o t a v i o
# -6-5-4-3-2-1

nome = 'gaviões'
print(nome[2])

print('o' in nome) # "O" esta entre as letras do nome
print('g' in nome)
print('M' in nome)
print(15 * '-')
print('ões' not in nome) #invertendo as expressões
print('zero' not in nome)

nome1 = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontar: ')

if encontrar in nome1:
    print(f'{encontrar} está em {nome1}')
else:
    print(f'{encontrar} não está em {nome1}')