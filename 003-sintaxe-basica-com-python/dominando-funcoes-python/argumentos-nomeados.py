def salvar_carro(ano, modelo, marca, placa):
    # salva carro mo banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca":"Fiat2", "modelo":"Palio2", "ano":1999-2, "placa":"ABC-1234-2"})


