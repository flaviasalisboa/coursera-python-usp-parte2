def encontra_impares(lista):
	if len(lista) == 0:
		return []
	listaImpares = lista.pop(0)
	if listaImpares % 2 != 0:
		return [listaImpares] + encontra_impares(lista)
	return encontra_impares(lista)

#def encontra_impares(lista):
#	listaImpares = []
#	if len(lista) > 0:
		# Retira o primeiro elemento da lista:
#		numero = lista.pop(0)
		# Verifica se o número é ímpar:
#		if numero % 2 != 0:
#			listaImpares.append(numero)
			# Faz a união do resultado atual com o retorno para o resto da lista:
#			listaImpares = listaImpares + encontra_impares(lista)
#	return listaImpares


#print(encontra_impares([1,7,13,10,12,21]))
#print(encontra_impares([1,7,13,10,12,16,21,3,9,11]))