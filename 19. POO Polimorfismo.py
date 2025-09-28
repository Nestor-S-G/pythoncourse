
class Coche():
	
	def desplazamiento(self):
		print("Se desplaza con 4 ruedas.")
		

class Moto():
	
	def desplazamiento(self):
		print("Se desplaza con 2 ruedas.")

class Camion():
	
	def desplazamiento(self):
		print("Se desplaza utilizando 6 ruedas.")


#Polimorfismo

def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

miVehiculo=Moto()

desplazamientoVehiculo(miVehiculo)

#Instancias

miVehiculo=Moto()

miVehiculo.desplazamiento()

miVehiculo2=Coche()

miVehiculo2.desplazamiento()

miVehiculo3=Camion()

miVehiculo3.desplazamiento()
