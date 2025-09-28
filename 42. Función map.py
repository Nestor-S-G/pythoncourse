#Aplica una función a cada elemento de una lista iterable (lista, tupla) y devuelve otra lista con el resultado

class Empleado:
	
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario
		
	def __str__(self):
		return"{} trabaja como {} y tiene un salario de {}€.".format(self.nombre, self.cargo, self.salario)
		

listaEmpleados=[

Empleado("Juan", "Director", 7500),
Empleado("Ana", "Presidenta", 8500),
Empleado("Antonio", "Administrativo", 2500),
Empleado("Sara", "Secretaria", 2700)

]

def calculo_comision(empleado):
	if(empleado.salario<3000): #Para que aplique la comisión a los salarios inferiores a 3000
		empleado.salario=empleado.salario*1.03
	return empleado

listaEmpleadosComision=map(calculo_comision, listaEmpleados)

for i in listaEmpleadosComision:
	print(i)
