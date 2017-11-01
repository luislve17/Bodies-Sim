import numpy as np

gBodies = []

class Body:
	def __init__(self, id_st, m, r_x, r_y, r_z, v_x, v_y, v_z, color):
		self.id = id_st
		self.mass = m
		self.r_x = r_x
		self.r_y = r_y
		self.r_z = r_z
		self.v_x = v_x
		self.v_y = v_y
		self.v_z = v_z
		self.color = color
		self.prepareNumpy()
	
	def prepareNumpy(self):
		# Preparando los vectores de operacion n_bodies para manipularlos con numpy
		self.r = []
		self.r.append(self.r_x)
		self.r.append(self.r_y)
		self.r.append(self.r_z)
		self.r = np.array(self.r)

		self.v = []
		self.v.append(self.v_x)
		self.v.append(self.v_y)
		self.v.append(self.v_z)
		self.v = np.array(self.v)

	def refreshInteraction(bodies_arr):
		global gBodies
		new_gBodies = []
		for b in bodies_arr:
			temp_body = b
			temp_body = Body.recalcBody(temp_body, b, bodies_arr)
			new_gBodies.append(temp_body)
		gBodies = new_gBodies

	def recalcBody(contenier, principal_body, interacting_bodies):
		dt = 5000
		G = 6.674e-11 # Constante de gravitacion universal
		a = np.array([.0,.0,.0]) # Aceleracion a acumular por cada cuerpo interactuando
		for b in interacting_bodies: # Para cada cuerpo en gBodies
			if b.id != principal_body.id: # Diferente al manipulado
				d = b.r - principal_body.r # r_j - r vector distancia entre vectores posicion
				a += d*((G*b.mass)/(np.linalg.norm(d)**3)) # Ecuacion de gravitacion universal (vectorial)
		# Actualizar parametros de temp_body
		contenier.v += a*dt
		contenier.r += contenier.v*dt
		return contenier

def main():
	b = Body("b1", 13, 1,2,-1,0,3,4, (0.5,0.2,0.45))
	print(b.v)

if __name__ == "__main__":
	main()