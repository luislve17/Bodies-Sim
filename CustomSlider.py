from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CustomSlider(QSlider):
	Nothing, Right, Left = range(3)
	def __init__(self):
		QSlider.__init__(self)
		self.direction = CustomSlider.Nothing
		self.last_value = self.value()/self.maximum()
		self.valueChanged.connect(self.getStatus)

	def getStatus(self):
		self.current_value = self.value()/self.maximum()
		# Revisamos la direccion en que se movio
		if self.current_value > self.last_value:
			self.direction = CustomSlider.Right
		elif self.current_value < self.last_value:
			self.direction = CustomSlider.Left

		# Actualizamos la direccion actual como la ultima establecida luego del cambio
		self.last_value = self.current_value
