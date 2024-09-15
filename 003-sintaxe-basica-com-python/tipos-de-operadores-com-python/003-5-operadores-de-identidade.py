# Operadores de identidade (Se ocupa a mesma região de memória)
# 
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
# >>> True

curso is not nome_curso
# >>> False

saldo is limite
# >>> False



a = 1
b = 1
print(a is b)
