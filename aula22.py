# Operadores lógicos 
# OR
# and (e) or (ou) not (não)  
# and - todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira é avaliada como falso e naql valor
# São consideradas falsy: 0, 0.0, '', False


# avalição de curtos circuitos
print(0 or False or 0 or 'abc' or True) # considera o preimeiro valor verdadeiro
senha = input('Senha: ') or 'Sem senha' 
print(senha)