def areaTriangulo(base, altura):
	
	"""
	Calcula el área de un triángulo.
	
	>>> areaTriangulo(3,6) #'se llama a la función y se pone debajo el resultado que debería dar.
	'El área del triángulo es: 9.0'
	
	>>> areaTriangulo(4,5)
	'El área del triángulo es: 10.0'
	
	"""
	
	return "El área del triángulo es: "+str(base*altura*.5)

import doctest
doctest.testmod()

print(areaTriangulo(2, 4))



