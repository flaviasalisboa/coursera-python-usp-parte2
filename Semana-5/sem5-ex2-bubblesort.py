# Semana 5 - Exercício 2 - Bubble sort (ordenação)

def bubble_sort(lista):
	fim = len(lista)
	for i in range(fim-1, 0, -1):
		for j in range(i): # vai do 0 até i-1
			if lista[j] > lista[j+1]:
				lista[j], lista[j+1] = lista[j+1], lista[j]
				print(lista)
	return lista 

#print(bubble_sort([5, 1, 4, 2]))
#print(bubble_sort([1, 2, 3, 5, 4, 0]))