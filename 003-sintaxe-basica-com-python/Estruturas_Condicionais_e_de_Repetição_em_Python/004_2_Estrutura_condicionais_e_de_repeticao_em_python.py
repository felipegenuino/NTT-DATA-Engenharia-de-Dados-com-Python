# Estruturas Condicionais (permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.)



saldo = 2000.0
saque = float(input("Informe o valor do saque: ") )


# ESTRUTURA IF ####################################
if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")


# IF ELSE #################################### 
if saldo >= saque:
    print("Realizando saque!")
else:
    print("saldo insificiente")



# ELIF #################################### 
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    # ...
elif opcao == 2:
    print("Exibindo o extrato ...")
else:
    sys.exit("Opção inválida")


