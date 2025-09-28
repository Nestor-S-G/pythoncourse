#Encapsular (__) sirve para que no se pueda modificar una propiedad desde fuera de la clase.

class Coche():
	
	#constructor
	def __init__(self):
		
	#propiedades. Los __ las encapsulan
		self.__largoChasis = 250 #cm
		self.__anchoChasis = 120
		self.__ruedas = 4 
		self.__enmarcha = False
	
	#comportamiento
	def arrancar(self,arrancamos): #método. Self es por defecto
		self.__enmarcha=arrancamos
		
		if(self.__enmarcha):
			chequeo=self.__chequeo_interno()
		
		if(self.__enmarcha and chequeo):
			return "El coche está en marcha."
			
		elif(self.__enmarcha and chequeo==False):
			return "Algo ha ido mal en el chequeo."
			
		else:
		    return "El coche está parado."

	def estado(self):
		print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis,"cm.")

	def __chequeo_interno(self):
		print("Se va a proceder a un chequeo interno.")
		
		self.gasolina="OK"
		self.aceite="ok"
		self.puertas="cerradas"
		
		if(self.gasolina=="OK" and self.aceite=="OK" and self.puertas=="cerradas"):
			return True
		else:
			False

miCoche=Coche() #objeto, 'instanciar una clase', una 'instanciación de clase' o ejemplarizar la clase.

print(miCoche.arrancar(True))
miCoche.estado()

print("---Segundo objeto---")



miCoche2 = Coche()
print(miCoche2.arrancar(False))

miCoche2.__ruedas=5 #No surte efecto al estar encapsulado

miCoche2.estado()
