# https://web.dio.me/course/tipos-de-operadores-com-python/learning/41df67fd-70a9-4bb1-b87f-34b129996013?back=/track/engenharia-dados-python&tab=undefined&moduleId=undefined
# São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de compraração com os operadores lógicos, exemplo: 
# op_comparacao + op_logico + op_comparacao ... N


# Exemplo
saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)
# >>> True

print(saque <= limite)
# >>>  False


# OPERADOR E (para dar True, as duas condições precisam ser True)
print(saldo >= saque and saque <= limite)

# OPERADOR OU (para dar False, as duas condições precisam ser False)
print(saldo >= saque or saque <= limite)


# Operador de negação
contatos_emergencia = []

not 1000 > 1500
# >>> True

not contatos_emergencia
# >>> True

not "saque 1500"
# >>> False

not " "
# >>> True


# PARENTESES
saldo2 = 1000
saque2 = 250
limite2 = 200
conta_especial = True

saldo2 >= saque2 and saque2 <= limite2 or conta_especial and saldo2 >= saque2
# >>> True

ex = (saldo2 >= saque2 and saque2 <= limite2) or (conta_especial and saldo2 >= saque2)
print (ex)
# >>> True


print("\nTabela verdade")
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
