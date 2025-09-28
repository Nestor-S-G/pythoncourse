print("Programa de becas")
print()
distancia = int(input("Distancia al centro (km): "))
hermanos = int(input("Número de hermanos: "))
salario = int(input("Salario anual (€): "))

if distancia > 40 and hermanos > 2 or salario <= 20000:
	print("Tiene derecho a beca.")
else:
	print("No tiene derecho a beca.")


print()
print("Asignaturas optativas")
print()
print("Neuroeconomía - Finanzas conductuales - Neuromarketing")
print()
opcion = input("Escribe la asignatura optativa escogida, tal cual está escrita en la lista superior: ")

asignatura = opcion.lower() #Para compensar el case sensitive

if asignatura in ("neuroeconomía", "finanzas conductuales", "neuromarketing"):
	print("Asignatura elegida: " + asignatura+".")
else:
	print("Asignatura escogida incorrecta.")
