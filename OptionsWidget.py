from PyQt4.QtGui import *
from OpenGlWidget import *

class OptionsWidget(QWidget):

	# Constructor
	def __init__(self, labels):
		# Constructor
		super().__init__()

		self.AnimFlag = False
		self.GuidesFlag = False
		self.VecFlag = False
		# Arreglo de botones radiales
		self.checkbox_arr = []
		
		# Inicializacion del arreglo de botones
		for st in labels:
			self.checkbox_arr.append(QCheckBox(st))

		# Organizacion del layout de botones
		self.OptionsLayout = QHBoxLayout()

		for bt in self.checkbox_arr:
			self.OptionsLayout.addWidget(bt)

		self.checkbox_arr[0].toggled.connect(self.setVectorFlag)
		# ToDo texturas
		self.checkbox_arr[2].toggled.connect(self.setAnimationFlag)
		self.checkbox_arr[3].toggled.connect(self.setGuidesFlag)
		
		self.setLayout(self.OptionsLayout)
	
	def setVectorFlag(self):
		self.VecFlag = not self.VecFlag
		OpenGlWidget.changeVecFlag(self.VecFlag)
	
	def setAnimationFlag(self):
		self.AnimFlag = not self.AnimFlag
		OpenGlWidget.changeAnimFlag(self.AnimFlag)

	def setGuidesFlag(self):
		self.GuidesFlag = not self.GuidesFlag
		OpenGlWidget.changeGuidesFlag(self.GuidesFlag)