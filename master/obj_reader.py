# Author: Samarth Chitgopekar
# Date: Oct 19, 2021
# Title: Obj File Handler
# Version: 1.0
# Link: https://github.com/Rad-hi/3D-Rendering-Desktop-App/blob/main/src/obj_files_handler.py

# Chitgopekar, S (Oct 19, 2021) Obj File Handler[Source Code] https://github.com/Rad-hi/3D-Rendering-Desktop-App/blob/main/src/obj_files_handler.py

from cmath import sin
from lib2to3.pgen2.token import OP
import time
import tkinter as Tk
from OpenGL import GL, GLU
from OpenGL.GL import shaders
from click import open_file
from pyopengltk import OpenGLFrame
import math
import re

from scipy.misc import face

Vertex = (    (1, -1, -1),    (1, 1, -1),    (-1, 1, -1),    (-1, -1, -1),
                 (1, -1, 1),    (1, 1, 1),    (-1, -1, 1),    (-1, 1, 1)    )

Edge = (    (0,1),    (0,3),    (0,4),    (2,1),    (2,3),    (2,7),
    (6,3),    (6,4),    (6,7),    (5,1),    (5,4),    (5,7)    )

rotX = 0
rotY = 0
rotZ = 3

rot_true = False #Runs when a function runs
func_ran = None

def extract_data(file):
     verticies = {}
     faces = []
     v = 1 # First vertex (one indexed)

     # Read more about how waveform (.obj) files are structured to understand
     # how this code exactly works, but shortly:
     #   * If the line starts with a "v", then that's a vertex and what follows is
     #     its X, Y, Z coordinates (foats)
     #   * If the line starts with a "f", then that's a face and what follows is
     #     the list of verticies to be connected to create a face
     #     (formatted a bit strangely though, I recommend checking an example)

     for line in file.readlines():
         if line[0:2] == "v ":
             verticies[v] = [[float(x)] for x in re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", line)]
             v += 1
         elif line[0:2] == "f ":
             faces.append([int(vertex.split("/")[0]) for vertex in line[2:-2].split(' ')])
     return verticies, faces

def Cube():
    GL.glBegin(GL.GL_LINES)
    for e in Edge:
        for v in e:
            GL.glVertex3fv(Vertex[v])
    GL.glEnd()

def obj_file(file_path):
    verts, faces = extract_data(open_file(file_path, "r"))
    return verts, faces

def draw_obj(modeldata):
    verts, faces = modeldata
    if len(faces[0]) == 3:
        GL.glBegin(GL.GL_TRIANGLES)
        for f in faces:
            for i in range(len(f)):
                GL.glVertex3fv(verts.get(f[i]))
        GL.glEnd()
    elif len(faces[0]) == 4:
        GL.glBegin(GL.GL_QUADS)
        for f in faces:
            for i in range(len(f)):
                GL.glVertex3fv(verts.get(f[i]))
        GL.glEnd()

class frame(OpenGLFrame):
    rot = 0
    moveY = 0
    def initgl(self): #When frame is created start
        GL.glViewport(0, 0, self.width, self.height)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluPerspective(90, self.width/self.height, 0.1, 100.0)
        GL.glClearColor(0.8, 0.9, 0.8, 0.0)
        self.start = time.time()
        self.nframes = 0
        self.modeldata = {
        "Weather":
            obj_file("master\\3D_Models\Cloud.obj"),
        "Topic":
            obj_file("master\\3D_Models\IsoSphere.obj"),
        "Microphone":
            obj_file("master\\3D_Models\Microphone.obj"),
        "News":
            obj_file("master\\3D_Models\\NewsPaper.obj"),
        "Date and Time":
            obj_file("master\\3D_Models\Clock.obj"),
        "Website":
            obj_file("master\\3D_Models\WiFi.obj"),
        "Application":
            obj_file("master\\3D_Models\\Rocket.obj"),
        "Email":
            obj_file("master\\3D_Models\\Email.obj"),
        }

    def redraw(self): #Draws frame
        # if self.rot >= 6.28:
        #     self.rot = 0

        self.rot += 0.01
        self.start = time.time()
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()
        GLU.gluLookAt(rotX, rotY, rotZ, 0, 0, 0, 0, 1, 0)

        GL.glTranslated(0, math.sin(self.rot), 0)
        GL.glRotated(30.0*self.rot, 0, 1, 0)


        tm = time.time() - self.start
        self.nframes += 1

        if func_ran in self.modeldata:
            draw_obj(self.modeldata[func_ran])
        else:
            Cube()

