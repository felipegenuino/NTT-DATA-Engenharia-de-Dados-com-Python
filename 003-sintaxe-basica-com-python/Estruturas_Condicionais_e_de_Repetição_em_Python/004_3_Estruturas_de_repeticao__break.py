# Comando break

# while 1
while True:
    numero = int(input("Informe um número: "))
    numero_da_sorte = 10
    if numero == numero_da_sorte:
        print("Acertou mizeravi ")
        break
    print("Tente novamente ")   

    print(numero)

 

# while 2
 while True:
   numero = int(input("Informe um número: "))
   if numero == 10:
       break
   if numero % 2 == 0:
       continue
   
   print(numero)




# Comando continue (Pares)
for numero in range(100):
    if numero % 2 == 0:
        continue

    print(numero, end=" ")

