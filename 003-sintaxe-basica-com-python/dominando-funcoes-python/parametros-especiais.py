# Parametros especiais 
# Por padrão, argumentos podem ser passados para uma função 
# Python tanto por posição quanto explicitamente pelo nome. 
# Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual 
# argumentos possam ser passados, assim um desenvolvedor precisa apenas olhar 
# para a definição da função para determinar se os itens são 
# passados por possição, por possição e nome, ou por nome.


# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    # ----------     -----------     --------
    # |             |              |
    # |             |              | - Keyword only
    # |             | - Positional or keyword
    # -- Positional only


# Essa sintaxe do Python define diferentes tipos de argumentos em uma função:

# pos1, pos2: Argumentos que são "positional only", indicados pelo /.
# pos_or_kwd: Pode ser passado tanto como argumento posicional quanto como keyword.
# kwd1, kwd2: São "keyword only", indicados pelo *.



# Atividade 1

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Chamadas da função
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # válido

# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido


# Explicação
# modelo, ano, placa: Argumentos "positional only" devido ao /.
# marca, motor, combustivel: Argumentos que podem ser passados como keywords.
# A primeira chamada da função é válida porque segue as regras de "positional only".
# A segunda chamada é inválida porque tenta passar argumentos "positional only" (modelo, ano, placa) como keywords.






