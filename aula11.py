# Precedencia dos operadores 
# Ordem que as contas são executadas pelo python
# 1. (n + n) 
# 2. **
# 3. * / // %
# 4. + - 
conta_1 = 1 + 1 ** 5 + 5  # errado - 1 ** 5 foi executada primeiro
print(conta_1) 

conta_2 = (1 + 1) ** (5 + 5) # certo
print(conta_2)

conta_3 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_3)