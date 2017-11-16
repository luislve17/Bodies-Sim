from PyQt4.QtGui import *
from Body import *
from n_bodies import *

class BodiesComboWidget(QWidget):
	def __init__(self, id_widget, masa_widget, pos_widget, vel_widget):
		super().__init__()
		self.entities_label = QLabel("Entidades")
		self.entities_combo = QComboBox()
		self.combo_layout = QVBoxLayout()
		self.combo_layout.addWidget(self.entities_label)
		self.combo_layout.addWidget(self.entities_combo)
		self.setLayout(self.combo_layout)
		self.fields_reference = [id_widget, masa_widget, pos_widget, vel_widget]
		self.entities_combo.currentIndexChanged.connect(self.load_body);
	
	def load_body(self):
		global gBodies
		for b in gBodies:
			if b.id == self.entities_combo.currentText():
				self.load_body_fields(b)
				break

	def load_body_fields(self, b):
		self.fields_reference[0].idTextBox.setText(b.id) # Cargar texto al campo de id
		self.fields_reference[1].fields_arr[0].setText(str(b.mass/(10**6))) # Cargar texto al campo de masa

		self.fields_reference[2].fields_arr[0].setText(str(b.r_x/(10**3))) # Cargar texto al campo de posicion
		self.fields_reference[2].fields_arr[1].setText(str(b.r_y/(10**3))) 
		self.fields_reference[2].fields_arr[2].setText(str(b.r_z/(10**3)))

		self.fields_reference[3].fields_arr[0].setText(str(b.v_x*(10**3))) # Cargar texto al campo de velocidad
		self.fields_reference[3].fields_arr[1].setText(str(b.v_y*(10**3)))
		self.fields_reference[3].fields_arr[2].setText(str(b.v_z*(10**3)))