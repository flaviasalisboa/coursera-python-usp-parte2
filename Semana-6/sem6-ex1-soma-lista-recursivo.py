def soma_lista(lista):
	n = len(lista)
	if n < 2:
		return lista[0]
	else:
		return lista[0] + soma_lista(lista[1:])

#print(soma_lista([1, 1, 1, 1, 1, 1, 1, 3]))
#print(soma_lista([14]))
#print(soma_lista([14, 3]))