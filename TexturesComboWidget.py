from PyQt4.QtGui import *
from random import *

class TexturesComboWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.textures_label = QLabel("Colores")
		self.textures_combo = QComboBox()
		self.textures_combo.setFixedSize(350,30)
		self.light_option = QCheckBox("Star");

		self.texture_module_layout = QVBoxLayout()
		self.util_layout = QHBoxLayout()
		
		self.textures_combo.addItem("Aleatorio")
		self.textures_combo.addItem("Rojo O.")
		self.textures_combo.addItem("Rojo C.")
		self.textures_combo.addItem("Azul O.")
		self.textures_combo.addItem("Azul C.")
		self.textures_combo.addItem("Verde O.")
		self.textures_combo.addItem("Verde C.")
		self.textures_combo.addItem("Amarillo O.")
		self.textures_combo.addItem("Amarillo C.")

		self.util_layout.addWidget(self.textures_combo)
		self.util_layout.addWidget(self.light_option)
		self.texture_module_layout.addWidget(self.textures_label)
		self.texture_module_layout.addLayout(self.util_layout)
		
		self.setLayout(self.texture_module_layout)

	def getContent(self):
		if self.textures_combo.currentText() == "Aleatorio":
			return (random(), random(), random())
		if self.textures_combo.currentText() == "Rojo O.":
			return (0.466, 0.074, 0.074)
		if self.textures_combo.currentText() == "Rojo C.":
			return (0.925, 0.713, 0.713)
		if self.textures_combo.currentText() == "Azul O.":
			return (0.047, 0.192, 0.513)
		if self.textures_combo.currentText() == "Azul C.":
			return (0.631, 0.717, 0.909)
		if self.textures_combo.currentText() == "Verde O.":
			return (0.023, 0.396, 0.145)
		if self.textures_combo.currentText() == "Verde C.":
			return (0.537, 0.843, 0.639)
		if self.textures_combo.currentText() == "Amarillo O.":
			return (0.388, 0.427, 0.090)
		if self.textures_combo.currentText() == "Amarillo C.":
			return (0.858, 0.909, 0.509)

	def getCheckState(self):
		return self.light_option.isChecked()