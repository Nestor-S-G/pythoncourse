#Bufle for - determinado

for i in [1,25,3]:
	print("FTW")
print()
for i in [1,25,3]:
	print(i)


for i in ["Lo que sea", "Whatever", 6]:
	print("Hola", end=" ")


#Verificar e-mail
contador=0

email_a_verificar = input("Introduzca dirección válida de e-mail: ")

for i in email_a_verificar:
	a = email_a_verificar.count("@")
	if a != 1:
		print("Email incorrecto")
	elif(i=="."):
		contador=contador+1

if contador == 1:
	print("Email correcto.")
else:
	print("Email incorrecto.")


#range

for i in range(5):
	print("Hallo")
