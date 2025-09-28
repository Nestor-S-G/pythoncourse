from io import open





archivo = open("archivo.txt", "r+") #asi se indica que es lectura y escritura

archivo.write("Comienzo del texto")

print(archivo.readlines())

lista_texto=archivo.readlines()

lista_texto[0]= "Esta línea ha sido incluída desde el exterior.\n"

archivo.seek(0)

archivo.writelines(lista_texto)

archivo.close()
