from PyQt4.QtCore import *
from PyQt4.QtGui import *

from OptionsWidget import *
from OpenGlWidget import *
from IdWidget import *
from ValuesWidget import *
from LoadBttWidget import *
from BodiesComboWidget import *
from TexturesComboWidget import *

class ToolsWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.id_input = IdWidget()
		self.masa_module = ValuesWidget("masa:", 1, ("10^6 kg"))
		self.pos_module = ValuesWidget("r (km):", 3, ("x", "y", "z"))
		self.vel_module = ValuesWidget("v (km/s):", 3, ("x", "y", "z"))
		self.visual_options = OptionsWidget(("Vector", "Texture", "Animate", "Guides"))
		self.bodies_combo = BodiesComboWidget(self.id_input, self.masa_module, self.pos_module, self.vel_module)
		self.textures_combo = TexturesComboWidget()

		self.widgets_arr = []
		self.widgets_arr.append(self.id_input)
		self.widgets_arr.append(self.masa_module)
		self.widgets_arr.append(self.pos_module)
		self.widgets_arr.append(self.vel_module)
		self.widgets_arr.append(self.bodies_combo)
		self.widgets_arr.append(self.textures_combo)
		self.load_button = LoadBttWidget(self.widgets_arr)
		
		
		self.tools_layout = QVBoxLayout()
		self.tools_layout.addWidget(self.bodies_combo)
		self.tools_layout.addWidget(self.id_input)
		self.tools_layout.addWidget(self.masa_module)
		self.tools_layout.addWidget(self.pos_module)
		self.tools_layout.addWidget(self.vel_module)
		self.tools_layout.addWidget(self.textures_combo)
		self.tools_layout.addWidget(self.load_button)
		self.tools_layout.addWidget(self.visual_options)
		
		self.setLayout(self.tools_layout)