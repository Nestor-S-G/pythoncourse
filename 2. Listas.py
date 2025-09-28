miLista = ["Mary", "Joseph", "Marty", "Hank", 'Rosemary', 'Jean-Marie']

print(miLista[-3])

print(miLista[0:2])
print(miLista[:2]) #análogo al anterior, si no se pone nada Python entiende que es 0
print(miLista[2:])

#Agregar elementos al final de una lista

miLista.append("Israel")
print(miLista[2:])

#En medio de la lista

miLista.insert(2, "Sandra")
print(miLista)

#Agregar varios elementos a una lista
miLista.extend(["Merle", "Anne", "Lucy"])
print(miLista)

print(miLista.index("Anne")) #Si hay varios igual, devuelve el índice del primero

print("Hank" in miLista)

miLista.remove("Anne")
print(miLista)


miLista2 = ["Abraham", "Benjamin"]
miLista3 = miLista+miLista2
print(miLista3)
miLista3.pop() #Elimina el último elemento de una lista
print(miLista3)

