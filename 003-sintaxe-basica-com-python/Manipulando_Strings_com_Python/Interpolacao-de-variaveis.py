# Introducao

# Em python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %, a segunda é utilizando o método format e a última é utilizando f strings. 
# A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro, por esse motivo iremos focar nas ultimas 2.

# OLD STYLE %
nome = "Felipe"
idade = 30
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))
# >>> Olá, me chamo Felipe. Eu tenho 30 anos de idade, trabalho com programador e estou matriculado no curso de Python.


## f-string (Mais Moderno)

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.")  
# >>> Olá, me chamo Felipe. Eu tenho 30 anos de idade, trabalho com programador e estou matriculado no curso de Python.


## Formatar strings com f-strings
PI = 3.14159

# Tamanho + numero de casas 0.0f
print(f"Valor de PI: {PI:.2f}")
# >>> "Valor de PI:  3.14"

print(f"Valor de PI: {PI:10.2f}")
# >>> "Valor de PI:      3.14"