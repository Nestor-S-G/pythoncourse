#Superclases y subclases

class vehiculos():
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False
		
	def arrancar(self):
		
		self.enmarcha=True
	
	def acelerar(self):
		self.acelera=True
	
	def frenar(self):
		self.frena = True
		
	def estado(self):
		print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha:",
		self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando:", self.frena)
		
		
#Herencia
class Furgoneta(vehiculos):
	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta va hasta los topes."
		else:
			return "La furgoneta is empty."


class Moto(vehiculos):
	hcaballito="Nope"
	def caballito(self):
		self.hcaballito = "Voy haciendo el caballito"
		
	def estado(self):
		print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha:",
		self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando:", self.frena, "\nCaballito:", self.hcaballito)


class EV(vehiculos): #Independiente, no hereda de las anteriores
	def __init__(self, marca, modelo):
		
		super().__init__(marca, modelo)
		
		self.autonomia= 200 #km

	def cargaNRG(self):
		self.cargando=True

miMoto=Moto("Honda", "CBR")

#miMoto.caballito()

miMoto.estado()


miFurgoneta= Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

#Herencia múltiple

class BiciElectrica(EV, vehiculos): #La primera clase indicada tiene preferencia, en este caso los EV
	pass
	

miBici=BiciElectrica("Orbea", "HIJK")
