def devuelve_ciudades(*ciudades): # El asterisco indica que el número de elementos es indeterminado
	for i in ciudades:
		yield i
		
ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "París")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))


def devuelve_ciudades(*ciudades): # El asterisco indica que el número de elementos es indeterminado
	for i in ciudades:
		for subi in i:
			yield subi
		
ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "París")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))


#Lo mismo con yield from para simplificar el codigo

def devuelve_ciudades(*ciudades): # El asterisco indica que el número de elementos es indeterminado
	for i in ciudades:
		yield from i
		
ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "París")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

