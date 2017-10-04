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

<center><b>Implementar la manipulación de parámetros para partículas desde la GUI de herramientas</b></center>

De la propuesta inicial, el _layout_ de la GUI estaba planeado como:


<p align="center"><img src="https://github.com/luislve17/Bodies-Sim/blob/master/readme_imgs/gui.png"/></p>

Para ello, se utilizaron dos herramientas:

* OpenGL
* PyQT: Extensión de python de la librería QT encargada de darnos un framework para implementar GUI's de manera práctica y multiplataforma.

___
## 2. Implementación
Por regla general, para crear un widget modificado que cumpla con los estándares de la clase _QWidget_, debemos extender dicha clase redefiniendo su constructor e implementando los métodos extras con normalidad

```python
from PyQt4.QtGui import *

class CustomWidget(QWidget):
	def __init__(self):
		Implementacion
		...
		...

	def extra(self):
		...
```

