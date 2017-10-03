import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ToolsWidget import *

class MainWindow(QMainWindow):
	#constructor
	def __init__(self):
		super().__init__()
		self.setWindowTitle("N Bodies Simulator")
		self.create_GUI()

	def create_GUI(self):
		# Widget principal generico
		self.mainWidget = QWidget()

		# Inicializacion de widgets
		self.opengl_canvas = OpenGlWidget(self.mainWidget)
		self.tools_module = ToolsWidget()

		# Definicion de layout principal
		self.main_layout = QHBoxLayout()
		self.main_layout.addWidget(self.opengl_canvas)
		self.main_layout.addWidget(self.tools_module)		
		
		# Seteando el widget principal y centrando en la ventana
		self.mainWidget.setLayout(self.main_layout)
		self.setCentralWidget(self.mainWidget)

def main():
	Simulator = QApplication(sys.argv) # Nueva aplicacion
	Simulator_window = MainWindow()
	Simulator_window.show()
	Simulator.exec_()

if __name__ == "__main__":
	main()