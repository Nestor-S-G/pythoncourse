miTupla = ("John", 13,1,1988)

print(miTupla[2])

#convertir tupla en lista

milista=list(miTupla)
print(milista)
print(miTupla)

#tupla en lista
miLista =  ["John", 13,1,1988]
mitupla = tuple(miLista)
print(mitupla)

print("John" in mitupla)

print(miTupla.count(1988))

print(len(miTupla))

TuplaSinPar = "Néstor", 1, 23 #empaquetado de tupla
print(TuplaSinPar)
nombre, mes, día = TuplaSinPar
print(nombre)
print(día)
