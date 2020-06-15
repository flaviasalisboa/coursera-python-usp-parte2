# Semana 6 - Exercício 3 - Programa Elefantes
# utilizando recursão

def incomodam(n):
	if n <= 0:
		return ""
	else:
		if n % 1 == 0:
			return "incomodam " + incomodam(n-1)
		else:
			return ""

def elefantes(n):
	if n == 1:
		return "Um elefante incomoda muita gente"
	else:
		if n == 2:
			return elefantes(n-1) + f"\n{n} elefantes "+ incomodam(n) + "muito mais" 
		else:
			if n > 2:
				frase1 = f"\n{n-1} elefantes incomodam muita gente"
				frase2 = f"\n{n} elefantes "+ incomodam(n) + "muito mais"
				return elefantes(n-1) + frase1 + frase2
			else:
				return ""

#print(elefantes(0))
#print(elefantes(1))
#print(elefantes(2))
#print(elefantes(3))
#print(elefantes(4))
