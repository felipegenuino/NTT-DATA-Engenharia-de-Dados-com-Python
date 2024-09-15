# Operadores de associação (São utilizados para verificar se um objeto está presente em uma sequencia)


curso = "Curso de Python"
frutas = ["laranja", "uva", "limao", "maça"]
saques = [1500, 100]

print("Python" in curso)
# >>> True

print("maça" in frutas)
# >>> True

print("maça" not in frutas)
# >>> False

print (200 in saques)
# >>> False