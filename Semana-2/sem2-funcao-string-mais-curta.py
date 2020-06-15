def menor_nome(listaNomes):
	listaTemp = []
	for i in listaNomes:
		limpaBrancos = i.strip()
		listaTemp.append(limpaBrancos)
		min = listaTemp[0]
		j = 1
		while j < len(listaTemp):
			if len(listaTemp[j]) < len(min):
				min = listaTemp[j]
			j += 1
	return min.capitalize()	 


#nomes = ["  ana   ","José", "Arquibaldo", " Alouhis"]
#nomes2 = [" Arquib   ","José", "ana", "Alouhis "]
#print(menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']))
#print(menor_nome(nomes))
#print(menor_nome(nomes2))
