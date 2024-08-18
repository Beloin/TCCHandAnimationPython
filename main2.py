import pygame
import sys

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertextxt = "./vertices.txt"
facestxt = "./faces.txt"

paints = [  # colors for our faces
    (0, 255, 0),  # green
    (255, 0, 0),  # red
    (255, 255, 0),  # yellow
    (0, 255, 255),  # cyan
    (0, 0, 255),  # blue
    (255, 255, 255),  # white
]


def get_list(txtname):
    listname = []
    with open(txtname) as f:
        for line in f:
            line = (
                line.rstrip(",\r\n").replace("(", "").replace(")", "").replace(" ", "")
            )
            row = list(line.split(","))
            listname.append(row)
    listname = [[float(j) for j in i] for i in listname]
    return listname


modelVerts = get_list(vertextxt)  # list of vertices
modelFaces = get_list(facestxt)  # list of faces

# TODO: How to move fingers?
def drawfaces():
    glClear(GL_COLOR_BUFFER_BIT or GL_DEPTH_BUFFER_BIT)  # clears each frame
    glBegin(GL_TRIANGLES)  # drawing method
    for eachface in modelFaces:  # each face in list of faces
        color = 0
        for eachvert in eachface:  # each point in each face
            color += 1
            if color > 5:
                color = 0
            # color = 5
            glColor3fv(paints[color])  # adding one solid color
            glVertex3fv(modelVerts[int(eachvert)])  # rendering triangles
    glEnd()


def main():
    pygame.init()
    display = (800, 800)  # set window
    pygame.display.set_caption("RENDERING OBJECT")
    FPS = pygame.time.Clock()  # fps func
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(50, 1, 0.1, 50)
    glTranslate(0, 0, -7)  # xyz
    glRotate(-90, 1, 0, 0)

    Left = False
    Right = False
    Up = False
    Down = False

    def moveOBJ():
        if Left:
            glRotate(-5, 0, 0, 5)
        if Right:
            glRotate(5, 0, 0, 5)
        if Up:
            glRotate(-5, 5, 0, 0)
        if Down:
            glRotate(5, 5, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_a:
                    Left = True
                if event.key == K_d:
                    Right = True
                if event.key == K_w:
                    Up = True
                if event.key == K_s:
                    Down = True
            if event.type == KEYUP:
                if event.key == K_a:
                    Left = False
                if event.key == K_d:
                    Right = False
                if event.key == K_w:
                    Up = False
                if event.key == K_s:
                    Down = False
        pygame.display.flip()
        drawfaces()
        moveOBJ()
        FPS.tick(60)


main()
