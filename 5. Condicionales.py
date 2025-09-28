print("Evaluación de notas")

nota_alumno = input("Nota: ") ##ACHTUN!! Los inputs siempre se toman como string

def evaluacion(nota):
	valoracion="aprobado"
	if nota < 5:
		valoracion="suspenso"
	elif nota > 10:
		valoracion = "nota incorrecta"
	return(valoracion)

print(evaluacion(float(nota_alumno)))




print("Verificación de acceso")

edad = int(input("Edad: "))

if edad < 18:
	print("Acceso denegado.")
elif edad >110:
	print("Edad incorrecta.")
else:
	print("Puede pasar.")



print()

edad = int(input("Introduzca edad: "))

if edad < 110 and edad >0:
	print("Edad correcta.")
else:
	print("Edad incorrecta.")

#Alternativa

if 0 < edad < 110:
	print("Edad correcta.")
else:
	print("Edad incorrecta")


salario_presidente = int(input("Salario presidente: "))
print("El salario del presidente es: "+str(salario_presidente))

salario_director = int(input("Salario director: "))
print("El salario del director es: "+str(salario_director))

salario_encargado = int(input("Salario encargado: "))
print("El salario del encargado es: "+str(salario_encargado))

salario_administrativo = int(input("Salario administrativo: "))
print("El salario del administrativo es: "+str(salario_administrativo))

if salario_administrativo < salario_encargado < salario_director < salario_presidente:
	print('Todo funciona correctamente.')
else:
	print('Algo falla en la empresa.')
	
	
