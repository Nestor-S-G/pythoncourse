#Super

class Persona():
	
	def __init__(self, nombre, edad, lugar):
		self.nombre=nombre
		self.edad=edad
		self.lugar=lugar
		
	def descripcion(self):
		print("Nombre:", self.nombre, " Edad:", self.edad, " Lugar de residencia:", self.lugar)

class Empleado(Persona):
	
	def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
		
		super().__init__(nombre_empleado, edad_empleado, residencia_empleado) 
		
		self.salario=salario
		self.antigüedad=antigüedad
		
	def descripcion(self):
		
		super().descripcion()
		print("Salario (€):", self.salario, ". Antigüedad en la empresa:", self.antigüedad)
		
		
Benito=Persona("Benito Lopera Perrote", "O más macho, o más.", "Madrid")

Benito.descripcion()

print(isinstance(Benito, Empleado)) #Comprueba si el objeto -Benito- es de la clase -Empleado-
print(isinstance(Benito, Persona)) #Comprueba si el objeto -Benito- es de la clase -Persona-, por el principio de sustitución
print(isinstance(Benito, Empleado)) #Comprueba si el objeto -Benito- es de la clase -Empleado-, por el principio de sustitución

