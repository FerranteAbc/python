primeiro_valor = input ("Digite um valor: ")
segundo_valor = input ("Digite outro valor: ")

if primeiro_valor > segundo_valor:
    print(primeiro_valor, 'é maior do que o', segundo_valor)
elif segundo_valor > primeiro_valor:
    print(segundo_valor, 'é maior do que o', primeiro_valor)
else:
    print('Você não digitou o valor correto')

