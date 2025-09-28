def compruebaMail(mail):
	
	"""
	Verifica la validez de una dirección de correo-e en función de la @.
	
	>>> compruebaMail('BMiK@FTW.es')
	True
	
	>>> compruebaMail('BMiKFTW.es@')
	False
	
	>>> compruebaMail('BMiKFTW.es')
	False
	
	>>> compruebaMail('BMiK@@FTW.es')
	False
	
	"""
	arroba=mail.count('@')
	
	if(arroba!=1 or mail.rfind("@")==(len(mail)-1) or mail.find("@")==0): #la última condición es redundante
		return False
	else:
		return True

import doctest
doctest.testmod()
