# Args e KWargs
# Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos (*args e **kwargs), o método recebe os valores como 
# tupla e dicionário respectivamente.



# POEMA
def exibir_poema(data_extenso, *args, **kwargs):
    text = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{text}\n\n{meta_dados}"
    print(mensagem)


    

exibir_poema("Sexta, 26 agosto 22","Zen of Python", "Beautiful is better than ugly.", author="Tim Peters", ano=1999)



