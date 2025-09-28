for letra in "Python":
	if letra == "h":
		continue
	print("Viendo la letra: " + letra)
	

nombre = "You are like mayberry, bitch"

contador = 0

for i in nombre:
	if i ==" ":
		continue
	contador +=1 # === a contador=contador+1

print(contador)
print(len(nombre)) #Esto devuelve todos los carácteres, incluído el espacio.



email=input("Introduzca email: ")

for i in email:
	
	if i=="@":
		arroba=True
		
		break

else:
	arroba=False
	
print(arroba)
