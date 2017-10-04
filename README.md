# Bodies Simulator

# DEADLINE 1: Implementación de la GUI y comunicación con OpenGL

## Fecha de entrega: 5-6 de Octubre

## Programa:
* De QWidget:
	* Introducción
	* Implementación
		* **IdWidget**
		* **ValuesWidget**
			* **CustomSlider**
		* **OptionsWidget**
		* **BodiesComboWidget**
		* **LoadBttWidget**
			* Funciones **connect()**
	* Integracion de **ToolsWidget**
	* Conexion a **OpenGlWidget**

* Del cálculo:
	* Clase Body

* Main

___
# A. De QWidget

## 1. Introducción
Para la presente entrega el objetivo a cumplir era el siguiente:

> **DEADLINE 1: Implementar la manipulación de parámetros para partículas desde la GUI de herramientas**

De la propuesta inicial, el _layout_ de la GUI estaba planeado como:

<p align="center"><img src="https://github.com/luislve17/Bodies-Sim/blob/master/readme_imgs/gui.png"/></p>

De la imagen se hace énfasis en dos partes principales: el "lienzo" de OpenGL y el módulo de herramientas que la controla. Para ello, se utilizaron dos herramientas:

* OpenGL
* PyQT: Extensión de python de la librería QT encargada de darnos un framework para implementar GUI's de manera práctica y multiplataforma.

De PyQt, la distribución de gráficos que utilizamos esta basado en BoxLayout, mediante la cual empujamos los widgets a la distribución en un orden específico para organizar los _widgets_ en la ventana principal

___
## 2. Implementación
Por regla general, para crear un widget modificado que cumpla con los estándares de la clase _QWidget_ debemos extender dicha clase redefiniendo su constructor e implementando los métodos extras con normalidad.

Para manipular los widgets primitivos que conformaran la clase solo hace falta definirlos como parámetros dentro de la clase extendida, luego se implementan métodos que permitan acceder a la información y así se manipula la totalidad del widget.

```python
from PyQt4.QtGui import *

class CustomWidget(QWidget):
	def __init__(self):
		super.__init__(self)
		self.mi_barra_text = QBarraTexto()
		self.mi_barra_text.ingresarTexto("texto")

	def metodo_extra(self):
		return self.mi_barra_text.obtenerTexto()
```

### 2.1 IdWidget

<p align="center"><img src="https://github.com/luislve17/Bodies-Sim/blob/master/readme_imgs/IdWidget.png"/></p>

``` python
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
```


### 2.2 ValuesWidget

<p align="center"><img src="https://github.com/luislve17/Bodies-Sim/blob/master/readme_imgs/ValuesWidget.png"/></p>

```python
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
```


### 2.2.1 CustomSlider

```python
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

```

## 2.3 OptionsWidget

```python
from PyQt4.QtGui import *

class OptionsWidget(QWidget):

	# Constructor
	def __init__(self, labels):
		# Constructor
		super().__init__()

		# Arreglo de botones radiales
		self.checkbox_arr = []
		
		# Inicializacion del arreglo de botones
		for st in labels:
			self.checkbox_arr.append(QCheckBox(st))

		# Organizacion del layout de botones
		self.OptionsLayout = QHBoxLayout()

		for bt in self.checkbox_arr:
			self.OptionsLayout.addWidget(bt)

		self.setLayout(self.OptionsLayout)
```

## 2.4 BodiesComboWidget
<p align="center"><img src="https://github.com/luislve17/Bodies-Sim/blob/master/readme_imgs/BodiesComboWidget.png"/></p>

```python
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

	
```

## 2.5 LoadBttWidget
<p align="center"><img src="https://github.com/luislve17/Bodies-Sim/blob/master/readme_imgs/LoadBttWidget.png"/></p>

```python
from PyQt4.QtGui import *
from Body import *

class LoadBttWidget(QWidget):
	def __init__(self, bindings_arr):
		super().__init__()
		self.widgets_arr = bindings_arr # Arreglo de comunicacion con widgets
		#self.bodies_arr = global_bodies # Arreglo de comunicacion con cuerpos

		self.load_btt = QPushButton("LOAD")
		self.load_btt.setMaximumSize(70, 40)
		self.button_layout = QHBoxLayout()
		self.button_layout.addWidget(self.load_btt)

		self.load_btt.clicked.connect(self.btnstate)

		self.setLayout(self.button_layout)
	
	def btnstate(self):
		self.id_content = self.widgets_arr[0].getContent() # id textbox
		self.mass_content = self.widgets_arr[1].getContent() # masa textbox
		self.pos_content = self.widgets_arr[2].getContent() # posicion textbox
		self.vel_content = self.widgets_arr[3].getContent() # velocidad textbox

		if not self.is_number(self.mass_content[0]):
			print("Error: Masa proporcionada no es numerica")
			return

		for l in self.pos_content:
			if not self.is_number(l):
				print("Error: Posicion proporcionada no es numerica")
				return
		
		for l in self.vel_content:
			if not self.is_number(l):
				print("Error: Velocidad proporcionada no es numerica")
				return

		for each in gBodies:
			if each.id == self.id_content:
				print("Error: Elemento ya existente")
				return

		# Aqui ya se puede utilizar los vectores
		self.newBody = Body(self.id_content, float(self.mass_content[0]),
					float(self.pos_content[0]), float(self.pos_content[1]),float(self.pos_content[2]),
					float(self.vel_content[0]), float(self.vel_content[1]), float(self.vel_content[2]))
		
		gBodies.append(self.newBody)

		self.widgets_arr[4].entities_combo.addItem("{}".format(self.newBody.id)) # Anadiendo un representante del elemento al combo
		
	def is_number(self, s):
		try:
			float(s)
			return True
		except ValueError:
			return False
```


### 2.5.1 Funciones **connect()**

```python
self.load_btt.clicked.connect(self.btnstate)
```

```python
def btnstate(self):
		self.id_content = self.widgets_arr[0].getContent() # id textbox
		self.mass_content = self.widgets_arr[1].getContent() # masa textbox
		self.pos_content = self.widgets_arr[2].getContent() # posicion textbox
		self.vel_content = self.widgets_arr[3].getContent() # velocidad textbox

		if not self.is_number(self.mass_content[0]):
			print("Error: Masa proporcionada no es numerica")
			return

		for l in self.pos_content:
			if not self.is_number(l):
				print("Error: Posicion proporcionada no es numerica")
				return
		
		for l in self.vel_content:
			if not self.is_number(l):
				print("Error: Velocidad proporcionada no es numerica")
				return

		for each in gBodies:
			if each.id == self.id_content:
				print("Error: Elemento ya existente")
				return

		# Aqui ya se puede utilizar los vectores
		self.newBody = Body(self.id_content, float(self.mass_content[0]),
					float(self.pos_content[0]), float(self.pos_content[1]),float(self.pos_content[2]),
					float(self.vel_content[0]), float(self.vel_content[1]), float(self.vel_content[2]))
		
		gBodies.append(self.newBody)

		self.widgets_arr[4].entities_combo.addItem("{}".format(self.newBody.id)) # Anadiendo un representante del elemento al combo
```

## 2.6 Integracion de **ToolsWidget**

```python
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from OptionsWidget import *
from OpenGlWidget import *
from IdWidget import *
from ValuesWidget import *
from LoadBttWidget import *
from BodiesComboWidget import *

class ToolsWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.id_input = IdWidget()
		self.masa_module = ValuesWidget("m:", 1, ("masa"))
		self.pos_module = ValuesWidget("r:", 3, ("x", "y", "z"))
		self.vel_module = ValuesWidget("v:", 3, ("x", "y", "z"))
		self.visual_options = OptionsWidget(("Trial", "Texture", "Animate"))
		self.bodies_combo = BodiesComboWidget()

		self.widgets_arr = []
		self.widgets_arr.append(self.id_input)
		self.widgets_arr.append(self.masa_module)
		self.widgets_arr.append(self.pos_module)
		self.widgets_arr.append(self.vel_module)
		self.widgets_arr.append(self.bodies_combo)
		self.load_button = LoadBttWidget(self.widgets_arr)
		
		
		self.tools_layout = QVBoxLayout()
		self.tools_layout.addWidget(self.bodies_combo)
		self.tools_layout.addWidget(self.id_input)
		self.tools_layout.addWidget(self.masa_module)
		self.tools_layout.addWidget(self.pos_module)
		self.tools_layout.addWidget(self.vel_module)
		self.tools_layout.addWidget(self.load_button)
		self.tools_layout.addWidget(self.visual_options)

		self.setLayout(self.tools_layout)
		self.setFixedSize(420, 480)
```

## 2.7 Conexion a **OpenGlWidget**
```python
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtOpenGL import *
from Body import *

angle = 0

class OpenGlWidget(QGLWidget):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(720, 480)
        self.anim_timer = QTimer(self) # Timer de animacion
        self.anim_timer.setInterval(25) # Ratio de actualizacion
        self.anim_timer.timeout.connect(self.updateGL) # Bindeo de la funcion a repintar
        self.anim_timer.start() # Inicializacion de la animacion

    def paintGL(self):
        # Funcion de dibujo para el contexto OpenGL
        global angle # Para el ejemplo

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(0, 0, -3.0)
        glRotatef(90, 1, 0, 0)
        glColor3f( .5, 1, 0.0 )
        glPolygonMode(GL_FRONT, GL_FILL)

        for b in gBodies:
            self.drawBody(b.r_x, b.r_y, b.r_z)

        glFlush()

        # Actualizacion de variables (por implementar)
        angle += 2

    def initializeGL(self):
        # Funcion de inicializacion de parametros
        glClearColor(0.0, 0.0, 0.0, 1.0) # Limpiar viewport con negro
        glClearDepth(1.0) # Fijamos la profundidad del fondo a su maximo
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()                    
        gluPerspective(45.0,1.33,0.1, 100.0) 
        glMatrixMode(GL_MODELVIEW)
        glutInit()

    def updateGL(self):
        self.update()

    def drawBody(self, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glRotatef(angle%360, 1, 0, 1)
        glutWireSphere(.25, 20, 20)
        glPopMatrix()
```

# B. Del cálculo

## Clase Body
```
gBodies = []

class Body:
	def __init__(self, id_st, m, r_x, r_y, r_z, v_x, v_y, v_z):
		self.id = id_st
		self.mass = m
		self.r_x = r_x
		self.r_y = r_y
		self.r_z = r_z
		self.v_x = v_x
		self.v_y = v_y
		self.v_z = v_z
```

# C. Main
```python
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
```