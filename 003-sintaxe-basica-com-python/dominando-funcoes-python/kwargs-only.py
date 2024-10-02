# Explicação
# O * indica que todos os argumentos devem ser passados como "keyword only".
# A primeira chamada da função é válida porque todos os argumentos são passados como keywords.
# A segunda chamada é inválida porque tenta passar argumentos sem nomeá-los, o que é proibido quando a função exige "keyword only" argumentos.



def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Chamadas da função
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # válido

# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido


