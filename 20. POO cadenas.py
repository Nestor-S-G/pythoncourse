nombreUsuario=input("Nombre de usuario: ")

print("El nombre de usuario es: ", nombreUsuario.capitalize())

edad = input("Introduce la edad: ")

while(edad.isdigit()==False):
	print("Introduzca valor numérico")
	edad = input("Introduce la edad: ")

	
if (int(edad)<18):
	print("No puede pasar.")
	
else:
	print("Puede pasar.")
