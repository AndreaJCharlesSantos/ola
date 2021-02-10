class Planta(object):
	def __init__(self = "", nombre = "",especie = "",temporada = ""):
		self._nombre = nombre
		self._especie = especie
		self._temporada = temporada
	def getnombre(self):
		return(self._nombre)
	def getespecie(self):
		return(self._especie)
	def gettemporada(self):
		return(self._temporada)

	def settemporada(self):
		return(self._temporada)
	def __eq__(self, otro):
		return self.nombre == otro.nombre
class Jardin(Planta):
	def __init__(self, j = 0, emplazamiento = "", lugar = "", nombre = ""):
		#self.emplazamiento = emplazamiento
		#self.lugar = lugar
		#self.numplantas = numplantas
		emplazamiento = lugar		
		p = []
		for i in p:
			p[i] = None

		numplantas = len(p)

	def Jardin(self, j):
		emplazamiento = j.emplazamiento
		numplantas = j.numplantas
		for i in range(0,100):
			if j.p[i] != None:
				p[i] = Planta(j.p[i].getnombre(),j.p[i].getespecie(),j.p[i].gettemporada())
			else:
				p[i] = None

	def Plantar(n = "", esp = "", tiempo = ""):
		if numplantas >= range(0,100):
			print("No caben más plantas en el jardín")
		else:
			lp = Planta(n, esp)
			lp.settemporada(tiempo)
			for i in range(0,100):
				if p[i] == None:
					p[i] = lp
					break
			numplantas += 1

	def Arrancar(nombre= "", esp = ""):
		if numplantas == 0:
			print("No quedan plantas en el jardín")
		else:
			tmp = Planta(nombre)
			p.remove(tmp)
			'''
			for i in range(0,100):
				if nombre == p[i].getnombre() and esp == p[i].getespecie():
					p[i].remove()
					p[i] = None
					numplantas -= 1
					break
					'''
#Inicio pedorro >:C
Prueba = Jardin()
Prueba.Jardin(100)
