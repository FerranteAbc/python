# Operações condicionais 

# if /      elif           /    else
# se /    se não se     /      se não
entrada = input('Você quer "entrar" ou "sair"? ') 

# Sempre dar um TAB para colocar o codigo no bloco
# ele executa cada bloco, ex digitou entrar ele só executa o If entrada
if entrada == 'entrar':
    print('Você entrou no sistema')

    print('Nos somos os Gaviões')
elif entrada  == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair')