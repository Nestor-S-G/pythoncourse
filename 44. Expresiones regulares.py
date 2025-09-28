import re

nombre1="Sandra López"

nombre2="Antonio Gómez"

nombre3= "María López"

nombre4="Jara Martínez"

nombre5="Lara Suárez"

cadena1="Jara López"

cadena2="546546546"

cadena3="a54654654"


if re.match("Sandra", nombre1):
	print("Nombre encontrado.")
else:
	print("No se ha encontrado.")


if re.match("Sandra", nombre1, re.IGNORECASE):#IGNORECASE desactiva la distinción mayúsula/minúscula
	print("Nombre encontrado.")
else:
	print("No se ha encontrado.")

if re.match(r"\d", cadena2):
	print("Número encontrado.")
else:
	print("No se ha encontrado.")

import re

cadena1 = "tu cadena aquí"  # Reemplaza esto con la cadena que quieres comprobar

if re.search(r"\d", cadena1): #search busca en toda la cadena, al contrario que march
    print("Número encontrado.")
else:
    print("No se ha encontrado.")

if re.search("López", nombre3): #search busca en toda la cadena, al contrario que march
    print("Número encontrado.")
else:
    print("No se ha encontrado.")
