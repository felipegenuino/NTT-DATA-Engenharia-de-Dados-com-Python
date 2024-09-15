# range(stop) -> range object
# range(start, stop[, step]) -> range object

range(4)
# >>> range(0,4)

print( list(range(4)) )
# >>> [0,1,2,3] 
# list converte em array

print( list(range(3,10)))
# >>> 3, 4, 5, 6, 7, 8, 9]


for numero in range(0,11):
    print(numero, end=" ")
# >>> 0 1 2 3 4 5 6 7 8 9 10



# range (0, 10, 2) start, stop, step
# Exibindo a tabuada de 5
for numero in range(0,51,5):
    print(numero, end=" ")

# >>> 0 1 2 3 4 5 6 7 8 9 10 0 5 10 15 20 25 30 35 40 45 50 


# Exibindo a tabuada de 2
for numero in range(0,21,2):
    print(numero, end=" ")
# >>> 0 2 4 6 8 10 12 14 16 18 20 
 