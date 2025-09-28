import re

cadena="Vamos a desaprender expresiones regulares en Python. Python es un lenguaje de programación sencillo."

print(re.search("aprender", cadena))

textoBuscar="Python"

if re.search(textoBuscar, cadena) is not None:
	print("He encontrado el texto.")
else:
	print("No he encontrado el texto")


textoEncontrado=re.search(textoBuscar, cadena)

print(textoEncontrado.start()) #Start nos dice en qué número de carácter aparece el texto buscado
print(textoEncontrado.end())
print(textoEncontrado.span())
print(re.findall(textoBuscar, cadena))
print(len(re.findall(textoBuscar, cadena)))
print()

lista_nombres=['Ana Gómez',
	'María Martín',
	'Sandra López',
	'Santiago Martín',
	'Sandra Martín']

lista_webs=['http://pildorasinformaticas.es',
			'ftp://pildorasinformaticas.es',
			'http://pildorasinformaticas.com',
			'ftp://pildorasinformaticas.com',
			'http://pildorasespañolas.com']
			
lista_personas=['mujeres',
				'hombres',
				'niñas',
				'niños']

for elemento in lista_nombres:
	if re.findall('^Sandra', elemento): #El ^ busca en todos el que empieza por Sandra
		print(elemento)

print()
for elemento in lista_nombres:
	if re.findall('Martín$', elemento): #El $ busca en todos los que acaba
		print(elemento)



for elemento in lista_webs:
	if re.findall('es$', elemento): 
		print(elemento)

for elemento in lista_webs:
	if re.findall('[ñ]', elemento): 
		print(elemento)

for elemento in lista_personas:
	if re.findall('niñ[oa]s', elemento): #también sirve para el mismo caracter con y sin tilde.
		print(elemento)


#ranges

lista_gente=['Ana',
			'Pedro',
			'María',
			'Rosa',
			'Sandra',
			'Celia']

print()
for elemento in lista_gente:
	if re.findall('[o-t]', elemento): 
		print(elemento)
print()
for elemento in lista_gente:
	if re.findall('[^o-t]', elemento): #^ niega el rango
		print(elemento)
