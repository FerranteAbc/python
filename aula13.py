#Formatação de String

nome = 'Pedro Henrique'
altura = 1.80
peso =  75
imc = peso / (altura * altura)

"f-strings"
# Usa as chaves {} nas variáveis para formartar o código
linha_1 = f'{nome} tem {altura:.2f} de altura' # 2.f (quantas casas decimais voce quer)
linha_2 = f'pesa, {peso}, quilos e seu IMC é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)