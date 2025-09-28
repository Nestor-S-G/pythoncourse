def divide():
	
	try:
	
		op1 = (float(input("Introdue el primer número: ")))
		op2 = (float(input("Introdue el 2º número: ")))
	
		print("La división es: " + str(op1/op2))
	
	except ValueError:
		
		print("El valor introducido es erróneo")
	
	except ZeroDivisionError:
		
		print("No se puede dividir entre 0.")
		
	finally: 
	
	print("Cálculo finalizado.")

divide()


def divide():
	
	try:
	
		op1 = (float(input("Introdue el primer número: ")))
		op2 = (float(input("Introdue el 2º número: ")))
	
		print("La división es: " + str(op1/op2))
	
	except:
		
		print("Ha ocurrido un error.") #Except general, no recomendable pero al menos el programa no se cae.
	
	
	print("Cálculo finalizado.")

divide()

