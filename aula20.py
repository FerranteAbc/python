# Operadores lógicos 
# and (e) or (ou) not (não)  
# and - todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira é avaliada como falso e naql valor
# São consideradas falsy: 0, 0.0, '', False
# Também existe o tipo none que é usado para representar um (Não valor)
# (AND) é usado para checar mais de uma condição

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
#if só será executado se for true
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

#--------------------------------------//---------------------------------//--------------------------------

# Avaliação de curto circuito
# ele para sempre no false e não checa mais nada pela frente
# São consideradas falsy: 0, 0.0, '', False
print(True and False and True)
print(bool(0))     