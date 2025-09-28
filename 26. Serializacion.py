import pickle

class vehiculo():
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

coche1=vehiculo("Mazda", "MX5")

coche2=vehiculo("Seat", "León")

coche3=vehiculo("Renault", "Megane")

coches=[coche1, coche2, coche3] #colección de objetos

fichero=open("coches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero) #Para borrarlo de la memoria


##Recuperacion

ficheroApertura=open("coches", "rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
	print(c.estado())
