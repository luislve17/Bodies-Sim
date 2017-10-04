from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtOpenGL import *
from Body import *
from random import *

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
        glColor3f( random(), random(), random() )
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