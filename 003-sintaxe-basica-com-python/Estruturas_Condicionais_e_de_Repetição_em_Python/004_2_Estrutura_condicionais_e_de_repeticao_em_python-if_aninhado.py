# IF Aninhado
# Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else.


# simulando banco se é conta normal ou universitária
conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:

    if saldo >= saque:
        print("saque realizado")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente")

elif conta_universitaria:

    if saldo >= saque:
        print("Saque realizado")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    print("Conta especial selecionada")

else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente")