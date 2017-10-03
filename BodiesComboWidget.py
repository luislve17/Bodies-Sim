from PyQt4.QtGui import *

class BodiesComboWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.entities_label = QLabel("Entidades")
		self.entities_combo = QComboBox()
		self.combo_layout = QVBoxLayout()
		self.combo_layout.addWidget(self.entities_label)
		self.combo_layout.addWidget(self.entities_combo)
		self.setLayout(self.combo_layout)

	