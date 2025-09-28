'''def area_triangulo(base, altura):
	
	return (base*altura)*.5

tri1=area_triangulo(5,7)

tri2=area_triangulo(9,6)

print(tri1)
print(tri2)'''


#Se puede simplificar la sintaxis con funciones lambda. Los : es como el return de la función tradicional
#No sirven para funciones con bucles o condicionales. Sólo devuelven un cálculo

area_triangulo=lambda base,altura:(base*altura)*.5

print(area_triangulo(7,5))
print(area_triangulo(9,6))


al_cubo=lambda numero:pow(numero, 3)

al_cuboAlt=lambda numero:numero**3

print(al_cubo(13))
print(al_cuboAlt(13))
print()

destacar_valor=lambda comision: "¡{}! €".format(comision)

comision_Ana=15585
print(destacar_valor(comision_Ana))
