import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ToolsWidget import *
from FileUtilities import *
from OpenGlWidget import *
from Body import *

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
		self.tools_module = ToolsWidget()		
		self.opengl_canvas = OpenGlWidget(self.mainWidget)
		
		# Definicion de layout principal
		self.main_layout = QHBoxLayout()
		self.main_layout.addWidget(self.opengl_canvas)
		self.main_layout.addWidget(self.tools_module)
		
		# Adicion de la barra superior
		bar = self.menuBar()
		op_archivo = bar.addMenu("Archivo")
		
		importar = QAction("Importar", self)
		importar.setShortcut("Ctrl + O")
		importar.triggered.connect(self.import_method)
		op_archivo.addAction(importar)
		
		exportar = QAction("Exportar", self)
		exportar.setShortcut("Ctrl + S")
		exportar.triggered.connect(self.export_method)
		op_archivo.addAction(exportar)
		# Fin modificacion
		
		
		# Seteando el widget principal y centrando en la ventana
		self.mainWidget.setLayout(self.main_layout)
		self.setCentralWidget(self.mainWidget)
		
	def import_method(self):
		import_name = QFileDialog.getOpenFileName(self, 'Importar archivo')
		if(import_name != ''):
			FileUtilities.importBodiesFile(import_name,self.tools_module.bodies_combo.entities_combo)
		
	def export_method(self):
		export_name = QFileDialog.getSaveFileName(self, 'Exportar archivo')
		if(export_name != ''):
			FileUtilities.exportBodiesFile(export_name)
			
def main():
	Simulator = QApplication(sys.argv) # Nueva aplicacion
	Simulator_window = MainWindow()
	Simulator_window.show()
	Simulator.exec_()

if __name__ == "__main__":
	main()
