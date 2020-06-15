def maiusculas(frase):
	strFim = ''
	for i in frase:
		asc2 = 65
		while asc2 <= 90:
			if (ord(i) == asc2):
				strFim = strFim + i
			asc2 += 1

	return strFim	 


#frase = "PrOgRaMaMoS em python!"
#print(maiusculas(frase))
