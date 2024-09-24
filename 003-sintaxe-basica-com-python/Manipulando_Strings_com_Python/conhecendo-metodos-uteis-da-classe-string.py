# Conhecer métodos úteis para manipular objetos do tipo string, como interpolar valores de variáveis e entender como funciona o fatiamento.



# etapa 1 - Conhecendo método úteis da classe string
# etapa 2 - Interpolação de variáveis
# etapa 3 - Fatiamento de string
# etapa 4 - String múltiplas linhas


# Introdução
# A classe String do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.
# Em algumas linguagens manipular sequências de caracteres não é um trabalho trivial, porém, em Pyton esse trabalho é muito simples.

curso = "pYtHon"

print(curso.upper())
# >>> PYTHON

print(curso.lower())
# >>> python

print(curso.title())
# >>> Python


curso2 = "    Python "

print(curso2.strip())
# >>> "Python"

print(curso2.lstrip())
# só remove o espaço da esquerda
# >>> "Python "

print(curso2.rstrip())
# só remove o espaço da direita
# >>> "    Python"


curso3 = "Python"

print(curso3.center(10, "#"))
# >>> "#Python#" 

print(".".join(curso3))
# >>> "P.y.t.h.o.n"




