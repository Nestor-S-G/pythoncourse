from io import open

archivo=open("archivo.txt", "w") #puede ser en modo lectura, escritura, append

frase = "Buen día para morir \nQue ya lo cantan Manowar."

archivo.write(frase)

archivo.close()


#Abrir en modo lectura

archivo=open("archivo.txt", "r")

lineas=archivo.readlines()

print(lineas)
print(lineas[0]) #Como es una lista, así se accede al primer elemento



#Append (para abrir en modo 'agregar', 'añadir'...

archivo=open("archivo.txt", "a")

archivo.write("\nBlack Metal ist Krieg.")

archivo.close()
