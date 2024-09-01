print(' ')
print('Saber qual tipo')
print('======')
preco = 10
print(type(preco)) 
print(type(10.0)) 
print(type(True)) 
print(type([1, True])) 
print(type({"name":"Felipe"})) 

print(' ')
print('Inteiro para FLoat')
print('======')
preco = 10
print(preco) 
preco = float(preco)
print(preco) 
preco = 10/2
print(preco)


print(' ')
print('======')
print('Float para Inteiro')
preco = 10.307676768
print(preco)

preco = int(preco)
print (preco)



print(' ')
print('======')
print('Conversão por divisão')
preco = 10
print(preco)

print (preco/2)

print(preco // 2)



print(' ')
print('======')
print('Numérico para string')
preco = 10.50
idade = 28

print(str(preco))

print(str(idade))


texto = f"idade:{idade} preço:{preco}"
print(texto)



print(' ')
print('======')
print('Erro de conversão')

preco = "python"
# print(float(preco))