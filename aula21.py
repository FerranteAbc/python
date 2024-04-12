# Operadores lógicos 
# OR
# and (e) or (ou) not (não)  
# and - todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira é avaliada como falso e naql valor
# São consideradas falsy: 0, 0.0, '', False

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')