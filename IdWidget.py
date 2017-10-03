from PyQt4.QtGui import *
from PyQt4.QtCore import *

class IdWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.idLabel = QLabel()
		self.idLabel.setText("ID: ")

		self.idTextBox = QLineEdit()

		self.IdLayout = QHBoxLayout()
		self.IdLayout.addWidget(self.idLabel)
		self.IdLayout.addWidget(self.idTextBox)

		self.setLayout(self.IdLayout)

	def getContent(self):
		return(self.idTextBox.text())