# Fatiamento de strings
# Fatiamento de strings é uma técnica utilizada para retornar 
# substrings (partes da string original), 
# informando inicio (start),  fim(stop), e passo(step): [start:stop[,step]]


name = "Felipe Genuino da Silva"

print(name[0])
# >>> F

print(name[:6])
# >>> Felipe

print(name[6:])
# >>> Genuino da Silva

print(name[6:14])
# >>>  Genuino

print(name[6:14:2])
# >>> eun
# >>> 2 são pulos do index

print(name[:])
# >>> Felipe Genuino da Silva

print(name[::-1])
# >>> avliS ad oniuneG epileF