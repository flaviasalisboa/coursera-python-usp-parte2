# Semana 4 - Exercício 2 - Busca sequencial

def busca(lista, elemento):
	for i in range(len(lista)):
		if lista[i] == elemento:
			return i
	return False

#print(busca([1, 2, 3, 4, 5, 6], 5))
#print(busca([1, 2, 3, 4, 5, 6], 8))