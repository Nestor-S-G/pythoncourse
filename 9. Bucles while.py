#El bucle while es un bucle indefinido. Cuidado con dar lugar a bucles infinitos.

i = 1

while i<=10:
	print("Ejecución " + str(i))
	i=i+1

print("Terminó la ejecución.")

edad=int(input("Introduzca edad: "))

while edad <0 or edad>110:
	print("Edad incorrecta. Try again: ")
	edad=int(input("Introduzca edad: "))

print("Edad correcta.")
print("Edad: "+ str(edad))


#Raíz cuadrada

import math

print("Programa para calcular raíz cuadrada")
num = int(input("Introduzca número: "))

intentos = 0

while num<0:
	print('No se puede hallar la raíz de un número negativo.')
	
	if intentos == 2:
		print("Número máximo de intentos fallidos.")
		break
	
	num = int(input("Introduzca número: "))
	if num <0:
		intentos = intentos + 1
		
if intentos <2:
	sol=math.sqrt(num)
	print("La raíz cuadrada de " + str(num) + " es " + str(sol)+'.')
