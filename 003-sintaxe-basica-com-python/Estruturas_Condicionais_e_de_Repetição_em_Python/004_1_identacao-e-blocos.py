# A estética
# Identar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da identação o interpretador consegue determinar onde um bloco de comando inicia e onde el termina.

def sacar(valor):
    saldo = 500
    saldoagora = (saldo - valor)
    print(f"Seu saldo é de R${saldo}")
    if saldo >= valor: 
        print( f"Sacado R${valor}")

    print(f"Seu saldo agora é de R${saldoagora}")
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(100)