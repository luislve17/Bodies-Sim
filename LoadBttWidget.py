from PyQt4.QtGui import *
from Body import *

light_created = False

class LoadBttWidget(QWidget):
	def __init__(self, bindings_arr):
		super().__init__()
		self.widgets_arr = bindings_arr # Arreglo de comunicacion con widgets

		self.load_btt = QPushButton("LOAD")
		self.load_btt.setMaximumSize(70, 40)
		self.button_layout = QHBoxLayout()
		self.button_layout.addWidget(self.load_btt)

		self.load_btt.clicked.connect(self.btnstate)

		self.setLayout(self.button_layout)
	
	def btnstate(self):
		global gBodies
		self.id_content = self.widgets_arr[0].getContent() # id textbox
		self.mass_content = self.widgets_arr[1].getContent() # masa textbox
		self.pos_content = self.widgets_arr[2].getContent() # posicion textbox
		self.vel_content = self.widgets_arr[3].getContent() # velocidad textbox
		self.color_content = self.widgets_arr[5].getContent() # Color del combo
		self.light_state = self.widgets_arr[5].getCheckState() # Estado del checkbox

		if not self.is_number(self.mass_content[0]):
			print("Error: Masa proporcionada no es numerica")
			return

		for l in self.pos_content:
			if not self.is_number(l):
				print("Error: Posicion proporcionada no es numerica")
				return
		
		for l in self.vel_content:
			if not self.is_number(l):
				print("Error: Velocidad proporcionada no es numerica")
				return

		for each in gBodies:
			if each.id == self.id_content:
				global light_created
				each.id = self.id_content
				each.mass = (10**6)*float(self.mass_content[0])
				each.r_x = (10**3)*float(self.pos_content[0])
				each.r_y = (10**3)*float(self.pos_content[1])
				each.r_z = (10**3)*float(self.pos_content[2])
				each.v_x = (0.001)*float(self.vel_content[0])
				each.v_y = (0.001)*float(self.vel_content[1])
				each.v_z = (0.001)*float(self.vel_content[2])
				each.color = self.color_content
				if self.light_state == True:
					if light_created == True:
						each.light = True
						light_created = False
					else:
						each.light = True
						light_created = True
				else:
					if each.light == True:
						each.light = False
						light_created = False
					else:
						each.light = False

				each.prepareNumpy()
				return

		# Aqui ya se puede utilizar los vectores
		if self.light_state == True:
			if light_created == True:
				self.light_created = False

		self.newBody = Body(self.id_content, (10**6)*float(self.mass_content[0]),
					(10**3)*float(self.pos_content[0]), (10**3)*float(self.pos_content[1]),(10**3)*float(self.pos_content[2]),
					(0.001)*float(self.vel_content[0]), (0.001)*float(self.vel_content[1]), (0.001)*float(self.vel_content[2]),
					self.color_content, self.light_state)
		
		gBodies.append(self.newBody)
		self.widgets_arr[4].entities_combo.addItem("{}".format(self.newBody.id)) # Anadiendo un representante del elemento al combo

	def is_number(self, s):
		try:
			float(s)
			return True
		except ValueError:
			return False

