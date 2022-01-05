fila = [chr(e) for e in range(97,122)]
columna = list(fila)
columna.sort(reverse = True)
tabla = dict(zip(fila,columna))

def atbash(palabra):
	cifrado = ""
	for letra in palabra:
		if letra != " ":
			cifrado += tabla[letra]
	return cifrado
while 1 == 1:
	mensaje = atbash(input("Inserte mensaje o 'quit' para salir: "))
	if mensaje == 'ieqf':
		break
	else:	
		print(mensaje)
	
