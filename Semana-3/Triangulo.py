
class Triangulo:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def perimetro(self):
		return self.a + self.b + self.c

	def tipo_lado(self):
		# isósceles - 2 lados iguais
		if (self.a == self.b and self.a != self.c and self.b != self.c) or (self.a == self.c and self.a != self.b and self.b != self.c) or (self.b == self.c and self.a != self.c and self.a != self.b):
			return 'isósceles'
		# equilátero - todos lados iguais
		if (self.a == self.b and self.a == self.c and self.b == self.c):
			return 'equilátero'
		# escaleno - todos lados diferentes
		if (self.a != self.b and self.a != self.c and self.b != self.c):
			return 'escaleno'

	def retangulo(self):
		quad1 = self.a * self.a
		quad2 = self.b * self.b
		quad3 = self.c * self.c
		if quad1 == (quad2 + quad3):
			return True
		if quad2 == (quad1 + quad3):
			return True
		if quad3 == (quad1 + quad2):
			return True
		return False

	def semelhantes(self, Triangulo):
		razao1 = self.a / Triangulo.a
		razao2 = self.b / Triangulo.b
		razao3 = self.c / Triangulo.c
		if (razao1 == razao2 and razao1 == razao3 and razao2 == razao3):
			return True
		else:
			return False 
