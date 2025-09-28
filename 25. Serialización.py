#Guardar en un fichero externo codificado en código binario una colección, objeto...

import pickle

lista =["Peter", "Anne", "Mary", "Elizabeth"]

fichero_binario=open("lista_nombres", "wb") #'write binary'

pickle.dump(lista,fichero_binario)

fichero_binario.close()

del(fichero_binario)

#para rescatar el fichero y leer la información

fichero=open("lista_nombres", "rb") #'read binary'

lista=pickle.load(fichero)

print(lista)
