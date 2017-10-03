from PyQt4.QtGui import *
from Body import *

class LoadBttWidget(QWidget):
	def __init__(self, bindings_arr):
		super().__init__()
		self.widgets_arr = bindings_arr # Arreglo de comunicacion con widgets
		#self.bodies_arr = global_bodies # Arreglo de comunicacion con cuerpos

		self.load_btt = QPushButton("LOAD")
		self.load_btt.setMaximumSize(70, 40)
		self.button_layout = QHBoxLayout()
		self.button_layout.addWidget(self.load_btt)

		self.load_btt.clicked.connect(self.btnstate)

		self.setLayout(self.button_layout)
	
	def btnstate(self):
		self.id_content = self.widgets_arr[0].getContent() # id textbox
		self.mass_content = self.widgets_arr[1].getContent() # masa textbox
		self.pos_content = self.widgets_arr[2].getContent() # posicion textbox
		self.vel_content = self.widgets_arr[3].getContent() # velocidad textbox

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
				print("Error: Elemento ya existente")
				return

		# Aqui ya se puede utilizar los vectores
		self.newBody = Body(self.id_content, float(self.mass_content[0]),
					float(self.pos_content[0]), float(self.pos_content[1]),float(self.pos_content[2]),
					float(self.vel_content[0]), float(self.vel_content[1]), float(self.vel_content[2]))
		
		gBodies.append(self.newBody)

		self.widgets_arr[4].entities_combo.addItem("{}".format(self.newBody.id)) # Anadiendo un representante del elemento al combo
		
	def is_number(self, s):
		try:
			float(s)
			return True
		except ValueError:
			return False

