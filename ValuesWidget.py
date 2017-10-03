from PyQt4.QtGui import *
from PyQt4.QtCore import *

from CustomSlider import *

class ValuesWidget(QWidget):
	def __init__(self, main_label, cant_fields, label_fields):
		super().__init__()
		self.main_label = QLabel()
		self.main_label.setText(main_label)
		self.num_fields = cant_fields

		self.fields_arr = [] # Arreglo de textbox's
		for i in range(cant_fields):
			self.textbox_i = QLineEdit()
			self.textbox_i.setMaximumSize(65, 30)
			self.fields_arr.append(self.textbox_i)

		self.labels_arr = [] # Arreglo de labels
		if cant_fields != 1:
			for i in range(cant_fields):
				self.label_i = QLabel(label_fields[i])
				self.label_i.setAlignment(Qt.AlignCenter)
				self.labels_arr.append(self.label_i)
		else:
			self.label_i = QLabel(label_fields)
			self.label_i.setAlignment(Qt.AlignCenter)
			self.labels_arr.append(self.label_i)

		self.regulation_bar = CustomSlider()
		self.regulation_bar.setOrientation(Qt.Horizontal)
		self.regulation_bar.setMinimum(0)
		self.regulation_bar.setMaximum(1000)
		self.regulation_bar.setValue(0)
		self.regulation_bar.valueChanged.connect(self.addToFields)

		# Layout principal del widget
		self.mainLayout = QHBoxLayout()
		# Layout interno de los campos numericos
		self.subLayout = QVBoxLayout()
		# Layout de campos y labels
		self.miniLayout_1 = QHBoxLayout()
		self.miniLayout_2 = QHBoxLayout()

		# Principal
		self.mainLayout.addWidget(self.main_label)
		self.mainLayout.addLayout(self.subLayout)
		self.mainLayout.addWidget(self.regulation_bar)

		# Campos y labels
		self.subLayout.addLayout(self.miniLayout_1)
		self.subLayout.addLayout(self.miniLayout_2)

		# Elementos
		for box in self.fields_arr:
			self.miniLayout_1.addWidget(box)

		for label in self.labels_arr:
			self.miniLayout_2.addWidget(label)

		self.setLayout(self.mainLayout)
	
	def getContent(self):
		self.fields = []
		
		for i in range(self.num_fields):
			self.fields.append(self.fields_arr[i].text())

		return self.fields

	def addToFields(self):
		if self.regulation_bar.direction == CustomSlider.Right:
			for each in self.fields_arr:
				if not self.is_number(each.text()):
					print("Error: Campo en", self.main_label.text(), "no numerico")
					return
				each.setText(str(float(each.text()) + 1))
		else:
			for each in self.fields_arr:
				if not self.is_number(each.text()):
					print("Error: Campo en", self.main_label.text(), "no numerico")
					return
				each.setText(str(float(each.text()) - 1))

	def is_number(self, s):
		try:
			float(s)
			return True
		except ValueError:
			return False