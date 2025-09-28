import math

def raizCuadrada(numeros):
	
	"""
	La función devuelve una lista con la raíz cuadrada de los elementos.
	
	>>> lista=[]
	>>> for i in [4, 9, 16]:
	...		lista.append(i) #Se usan los 3 puntos para anidar
	
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0]
	
	>>> lista=[]
	>>> for i in [4, -9, 16]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	Traceback (most recent call last):
		...
	ValueError: math domain error

	"""
	
	return [math.sqrt(n) for n in numeros]


print(raizCuadrada([9, 16, 25, 36, 39]))

import doctest
doctest.testmod()
