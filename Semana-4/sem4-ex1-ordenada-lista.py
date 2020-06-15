def selecao_direta(lista):
	fim = len(lista)
	for i in range(fim-1):
		posicao_do_minimo = i
		for j in range(i+1, fim):
			if lista[j] < lista[posicao_do_minimo]:
				posicao_do_minimo = j
		# invertendo os dois de posição
		lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
	return lista

def ordenada(lista):
	listaTemp = lista[:]
	listaOrdenada = selecao_direta(listaTemp)
	if listaOrdenada == lista:
		return True
	else:
		return False

#lista1 = [1, 2, 3, 4, 5]
#lista2 = [9, 8, 5, 6, 2]
#print(ordenada(lista1))
#print(ordenada(lista2))