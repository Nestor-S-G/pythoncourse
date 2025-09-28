#Forman parte de las llamadas funciones de orden superior

def numero_par(num):
	if num % 2==0:
		return True


numeros=[17, 24, 39, 8, 51, 92]

print(list(filter(numero_par, numeros)))

#con lambda

print(list(filter(lambda numero_par: numero_par%2==0, numeros)))



class Empleado:
	
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario
		
	def __str__(self):
		return"{} que trabaja como {} y tiene un salario de {}€".format(self.nombre, self.cargo, self.salario)
		

listaEmpleados=[

Empleado("Juan", "Director", 75000),
Empleado("Ana", "Presidenta", 85000),
Empleado("Antonio", "Administrativo", 25000),
Empleado("Sara", "Secretaria", 27000)

]

salarios_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for i in salarios_altos:
	print(i)
