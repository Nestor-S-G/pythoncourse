def evaluaEdad(edad):
	
	if edad<0:
		raise TypeError("No se permiten edades negativas.")
	
	if edad<20:
		return "Eres muy joven."
	elif edad <40:
		return "Eres joven."
	elif edad <65:
		return "Eres maduro."
	elif edad <100:
		return "Cuídate..."

print(evaluaEdad(35))

import math

def calculaRaiz(num1):
	if num1 < 0:
		raise ValueError("Las raíces de un número negativo no están definidas")
	else:
		return math.sqrt(num1)
		
op1=(int(input("Introduzca un número: ")))

try:
	print(calculaRaiz(op1))
	
except ValueError as ErrorNumeroNegativo:
	
	print(ErrorNumeroNegativo)

print()
