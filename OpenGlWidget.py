from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtOpenGL import *
from Body import *
from random import *

# Angulo de animacion para la presentacion
angle = 0
# Bandera de control para encender o apagar la animacion
gAnimFlag = False
# Vector observador
observador = [0,0,20]
# Valores de orientacion del observador
angle_x = 0
angle_y = 0
# Vector booleano para las teclas W,A,S,D,UP,DOWN,LEFT,RIGHT
key_handler = [False, False, False, False, False, False, False, False]

class OpenGlWidget(QGLWidget):
	def __init__(self, parent=None):
		QGLWidget.__init__(self, parent)
		self.setMinimumSize(720, 600)

		self.setFocusPolicy(Qt.StrongFocus)

		self.anim_timer = QTimer(self) # Timer de animacion
		self.anim_timer.setInterval(25) # Ratio de actualizacion
		self.anim_timer.timeout.connect(self.updateGL) # Bindeo de la funcion a repintar
		self.anim_timer.start() # Inicializacion de la animacion
		
		self.x = 0
    	
	def changeAnimFlag(b):
		global gAnimFlag
		gAnimFlag = b
    
	def paintGL(self):
		# Funcion de dibujo para el contexto OpenGL
		global angle # Para el ejemplo
		global gBodies

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		
		glPolygonMode(GL_FRONT, GL_FILL)

		glTranslatef(-observador[0], -observador[1], -observador[2])
		glRotatef(angle_x, 1,0,0)
		glRotatef(angle_y, 0,1,0)
		
		self.drawAxis()
				
		for b in gBodies:
			glColor3f(b.color[0], b.color[1], b.color[2])
			self.drawBody(b.r)

		glFlush()

		# Actualizacion de variables y animacion
		global gAnimFlag
		if gAnimFlag:
			Body.refreshInteraction(gBodies)
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
		# Manejar teclas
		OpenGlWidget.read_keys()
		self.update()
    	
	def drawBody(self, r): # r: vector posicion
		glPushMatrix()
		glTranslatef(r[0]/10**3, r[1]/10**3, r[2]/10**3)
		glRotatef(angle%360, 1, 0, 1)
		glutWireSphere(.1, 20, 20)
		glPopMatrix()
		
	def drawAxis(self):
		glPushMatrix()
		glBegin(GL_LINES)
	
		glColor3f(1,0,0) # X Rojo
		glVertex3f(100,0,0)
		glVertex3f(0,0,0)
		glColor3f(0.886, 0.5059, 0.5059) # -X Rosado
		glVertex3f(0,0,0)
		glVertex3f(-100,0,0)
		
		glColor3f(0,0,1) # Y Azul
		glVertex3f(0,100,0)
		glVertex3f(0,0,0)
		glColor3f(0.47, 0.639, 0.7372) # -Y Celeste
		glVertex3f(0,0,0)
		glVertex3f(0,-100,0)
		
		glColor3f(0,1,0) # Z Verde
		glVertex3f(0,0,100)
		glVertex3f(0,0,0)
		glColor3f(0.51, 0.807, 0.517) # -Z Verde claro
		glVertex3f(0,0, 0)
		glVertex3f(0,0,-100)
		
		glEnd()
		glPopMatrix()
			
	def keyPressEvent(self, event):
		self.on_key(event)
		event.accept()

	def keyReleaseEvent(self, event):
		self.off_key(event)
		event.accept()
	
	def wheelEvent(self,event):
		self.wheel_handler(event)
		event.accept()

	def on_key(self, event):
		if event.key() == Qt.Key_W:
			key_handler[0] = True
		if event.key() == Qt.Key_A:
			key_handler[1] = True
		if event.key() == Qt.Key_S:
			key_handler[2] = True
		if event.key() == Qt.Key_D:
			key_handler[3] = True
			
		if event.key() == Qt.Key_Up:
			key_handler[4] = True
		if event.key() == Qt.Key_Down:
			key_handler[5] = True
		if event.key() == Qt.Key_Left:
			key_handler[6] = True
		if event.key() == Qt.Key_Right:
			key_handler[7] = True

	def off_key(self, event):
		if event.key() == Qt.Key_W:
			key_handler[0] = False
		if event.key() == Qt.Key_A:
			key_handler[1] = False
		if event.key() == Qt.Key_S:
			key_handler[2] = False
		if event.key() == Qt.Key_D:
			key_handler[3] = False
			
		if event.key() == Qt.Key_Up:
			key_handler[4] = False
		if event.key() == Qt.Key_Down:
			key_handler[5] = False
		if event.key() == Qt.Key_Left:
			key_handler[6] = False
		if event.key() == Qt.Key_Right:
			key_handler[7] = False
	
	def wheel_handler(self, event):
		# Control de profundidad con la rueda del mouse
		observador[2] = observador[2] - event.delta()/480
			
	def read_keys():
		global key_handler
		global angle_x
		global angle_y
		# Traslacion
		if key_handler[0]: # W
			observador[1] += .1
		if key_handler[1]: # A
			observador[0] -= .1
		if key_handler[2]: # S
			observador[1] -= .1
		if key_handler[3]: # D
			observador[0] += .1
		# Rotacion
		if key_handler[4]: # UP
			angle_x -= 2
		if key_handler[5]: # DOWN
			angle_x += 2
		if key_handler[6]: # LEFT
			angle_y -= 2
		if key_handler[7]: # RIGHT
			angle_y += 2
			