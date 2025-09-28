import Modulos

class Areas:

	def areaCuadrado(lado):
		'''Calcula el área de un cuadrado elevando al cuadrado el lado pasado por parámetro.'''
	
		return "El área del cuadrado es: " + str(lado*lado)

	def areaTriangulo(base, altura):
		return "El área del triángulo es: " + str((base*altura)*.5)



#print(areaCuadrado.__doc__) #Esto imprime la 'documentación' de la función
#help(areaCuadrado) # Si no está dentro de una clase
help(Areas.areaCuadrado)

