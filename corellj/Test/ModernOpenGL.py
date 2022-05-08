from OpenGL import GL, GLU
import OpenGL.GL.shaders
import tkinter
import tkinter as Tk
from pyopengltk import OpenGLFrame
import glm

vertices = glm.array(glm.float32,
        -0.5, -0.5, 0.0, # left  
         0.5, -0.5, 0.0, # right 
         0.0,  0.5, 0.0  # top
        )
VAO = GL.glGenVertexArrays(1)
VBO = GL.glGenBuffers(1)

class ShaderFrame(OpenGLFrame):
    def initgl(self):
        GL.glBindVertexArray(VAO)

        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, vertices.nbytes, vertices.ptr, GL.GL_STATIC_DRAW)

        GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 3 * glm.sizeof(glm.float32), None)
        GL.glEnableVertexAttribArray(0)

        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
        
        GL.glBindVertexArray(0)

    def redraw(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        GL.glBindVertexArray(VAO)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)

def main():
    window = Tk.Tk()
    m_canvas = ShaderFrame(window, width=600, height=400)
    m_canvas.pack(fill=Tk.BOTH, expand=Tk.YES)
    m_canvas.animate = 1
    m_canvas.mainloop()

if __name__ == '__main__':
    main()