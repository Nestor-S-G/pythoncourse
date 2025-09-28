midicc = {"Deutschland":"Berlin", "Francia": "París", "UK":"London", "España" : "Madrid"}
midicc["Italia"] = "Roma" #Añadir un elemento. Para modificar elementos, se sobreescriben sin más
print(midicc["Deutschland"])
print(midicc)

#Eliminar elementos del diccionario

del midicc["UK"]
print(midicc)

midicc = {"Deutschland":"Berlin", 18: "Julio", "España" : 1492}
print(midicc)


#Crear un diccionario desde una tupla
miTupla = ["España", "Deutschland", "United Kingdom", "Francia"]
midic = {miTupla[0] : "Madrid", miTupla[1] : "Berlin", miTupla[2]: "London", miTupla[3]: "París"}
print(midic)
print(midic["España"])
print(midic[miTupla[0]])

#Diccionario con tupla

diccionarioTupla = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993, 1996, 1997, 1998]}
print(diccionarioTupla["anillos"])

#Diccionario con diccionario

diccionarioTupla = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993, 1996, 1997, 1998]}}
print(diccionarioTupla["anillos"])
print(diccionarioTupla.keys())
print(diccionarioTupla.values())
print(len(diccionarioTupla))
