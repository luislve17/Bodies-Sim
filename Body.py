gBodies = []

class Body:
	def __init__(self, id_st, m, r_x, r_y, r_z, v_x, v_y, v_z):
		self.id = id_st
		self.mass = m
		self.r_x = r_x
		self.r_y = r_y
		self.r_z = r_z
		self.v_x = v_x
		self.v_y = v_y
		self.v_z = v_z