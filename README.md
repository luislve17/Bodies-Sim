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
	* n_bodies

___

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
<p align="center"><img src="https://github.com/luislve17/Bodies-Sim/blob/master/readme_imgs/OptionsWidget.png"/></p>

## 2.4 BodiesComboWidget
<p align="center"><img src="https://github.com/luislve17/Bodies-Sim/blob/master/readme_imgs/BodiesComboWidget.png"/></p>

## 2.5 LoadBttWidget
<p align="center"><img src="https://github.com/luislve17/Bodies-Sim/blob/master/readme_imgs/LoadBttWidget.png"/></p>

### 2.5.1 Funciones **connect()**

## 2.6 Integracion de **ToolsWidget**

## 2.7 Conexion a **OpenGlWidget**