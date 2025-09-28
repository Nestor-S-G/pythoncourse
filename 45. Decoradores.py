#Los decoradores agregan las funcionalidades a las funcionalidades de tu programa de golpe, en lugar de tener que hacerlo una a una.

def funcionDecoradora(funcionParametro):
	
	def funcionInterior(*args, **kwargs): #args es una convenció, lo importante es el * y los **
		
		#Acciones adicionales que decoran
		
		print("Vamos a realizar un cálculo: ")
		
		funcionParametro(*args, **kwargs)
		
		#Acciones adicionales que decoran
		
		print("Hemos terminado el cálculo.")

	return funcionInterior


@funcionDecoradora #Esto hace que al llamar a la función decoradora le añada sus funcionalidades
def suma(num1, num2, num3):
	print(num1+num2+num3)


@funcionDecoradora 
def resta(num1, num2):
	print(num1-num2)

@funcionDecoradora 
def potencia(base, exponente):
	print(pow(base, exponente))

#Llamada de las funciones
suma(7,5,8)
print()
resta(12,10)
print()
potencia(base=5,exponente=3)


