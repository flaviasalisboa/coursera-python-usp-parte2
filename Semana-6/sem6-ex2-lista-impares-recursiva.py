# Semana 6 - Exercício 2 - Encontra apenas os ímpares
# da lista - com recursão

def encontra_impares(lista):
	if len(lista) == 0:
		return []
	listaImpares = lista.pop(0)
	if listaImpares % 2 != 0:
		return [listaImpares] + encontra_impares(lista)
	return encontra_impares(lista)

#print(encontra_impares([1,7,13,10,12,21]))
#print(encontra_impares([1,7,13,10,12,16,21,3,9,11]))