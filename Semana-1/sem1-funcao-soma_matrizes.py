# Semana 2 - Exercício 2 - Soma duas matrizes de mesma dimensão

def soma_matrizes(m1, m2):
	matrizSoma = []
	numRows = len(m1) 
	numCols = len(m1[0])
	numRows2 = len(m2)
	numCols2 = len(m2[0])
	if (numRows == numRows2) and (numCols == numCols2):
		for i in range(numRows):
			# Cria uma nova linha na matriz_soma
			matrizSoma.append([])
			for j in range(numCols):
				# Soman os elementos do mesmo índice e gravam na matrizSoma
				soma = m1[i][j] + m2[i][j]
				matrizSoma[i].append(soma)
		print("soma_matrizes(m1, m2) =>", end=' ')
		return matrizSoma
	else:
		print("soma_matrizes(m1, m2) =>", end=' ')
		return False


#m1 = [[1, 2, 3], [4, 5, 6]]
#m2 = [[2, 3, 4], [5, 6, 7]]
#soma = soma_matrizes(m1, m2)
#print(soma)
