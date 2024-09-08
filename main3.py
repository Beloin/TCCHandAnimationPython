import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import pyrr
from TextureLoader import load_texture
from ObjLoader import ObjLoader
from typing import List

from model import Model

vertex_src = """
# version 330

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
layout(location = 2) in vec3 a_normal;

uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;

out vec2 v_texture;

void main()
{
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    v_texture = a_texture;
}
"""

fragment_src = """
# version 330

in vec2 v_texture;

out vec4 out_color;

uniform sampler2D s_texture;

void main()
{
    out_color = texture(s_texture, v_texture);
}
"""

# Uniform Location
proj_loc = None


# glfw callback functions
def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    projection = pyrr.matrix44.create_perspective_projection_matrix(
        45, width / height, 0.1, 100
    )
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

    # initializing glfw library


# TODO: remove unecessary model_loc
def animate_models(window, model_loc, models: List[Model]):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for model in models:
        rot_y = pyrr.Matrix44.from_y_rotation(0.8 * glfw.get_time())
        a3dmodel = pyrr.matrix44.multiply(rot_y, model.get_pos())

        # draw the chibi character
        glBindVertexArray(model.get_VAO())
        glBindTexture(GL_TEXTURE_2D, model.get_texture())
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, a3dmodel)  # Or model.get_pos()
        glDrawArrays(GL_TRIANGLES, 0, len(model.get_indices()))

    glfw.swap_buffers(window)


# TODO: Remove mode_lod
def animate(window, model_loc, models: List[Model]):
    while not glfw.window_should_close(window):
        animate_models(window, model_loc, models)


def main():
    # initializing glfw library
    if not glfw.init():
        raise Exception("glfw can not be initialized!")

    # creating the window
    window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

    # check if window was created
    if not window:
        glfw.terminate()
        raise Exception("glfw window can not be created!")

    # set window's position
    glfw.set_window_pos(window, 400, 200)

    # set the callback function for window resize
    glfw.set_window_size_callback(window, window_resize)

    # make the context current
    glfw.make_context_current(window)
    chibi_indices, chibi_buffer = ObjLoader.load_model("texture_test.obj")
    monkey_indices, monkey_buffer = ObjLoader.load_model("texture_test2.obj")

    shader = compileProgram(
        compileShader(vertex_src, GL_VERTEX_SHADER),
        compileShader(fragment_src, GL_FRAGMENT_SHADER),
    )

    VAO = glGenVertexArrays(2)
    VBO = glGenBuffers(2)

    # Chibi VAO
    glBindVertexArray(VAO[0])
    # Chibi Vertex Buffer Object
    glBindBuffer(GL_ARRAY_BUFFER, VBO[0])
    glBufferData(GL_ARRAY_BUFFER, chibi_buffer.nbytes, chibi_buffer, GL_STATIC_DRAW)

    # chibi vertices
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(
        0, 3, GL_FLOAT, GL_FALSE, chibi_buffer.itemsize * 8, ctypes.c_void_p(0)
    )
    # chibi textures
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(
        1, 2, GL_FLOAT, GL_FALSE, chibi_buffer.itemsize * 8, ctypes.c_void_p(12)
    )
    # chibi normals
    glVertexAttribPointer(
        2, 3, GL_FLOAT, GL_FALSE, chibi_buffer.itemsize * 8, ctypes.c_void_p(20)
    )
    glEnableVertexAttribArray(2)

    # Monkey VAO
    glBindVertexArray(VAO[1])
    # Monkey Vertex Buffer Object
    glBindBuffer(GL_ARRAY_BUFFER, VBO[1])
    glBufferData(GL_ARRAY_BUFFER, monkey_buffer.nbytes, monkey_buffer, GL_STATIC_DRAW)

    # monkey vertices
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(
        0, 3, GL_FLOAT, GL_FALSE, monkey_buffer.itemsize * 8, ctypes.c_void_p(0)
    )
    # monkey textures
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(
        1, 2, GL_FLOAT, GL_FALSE, monkey_buffer.itemsize * 8, ctypes.c_void_p(12)
    )
    # monkey normals
    glVertexAttribPointer(
        2, 3, GL_FLOAT, GL_FALSE, monkey_buffer.itemsize * 8, ctypes.c_void_p(20)
    )
    glEnableVertexAttribArray(2)

    textures = glGenTextures(2)
    load_texture("texture_test.png", textures[0])
    load_texture("texture_test.png", textures[1])

    glUseProgram(shader)
    glClearColor(0, 0.1, 0.1, 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # TODO: Add transformation here
    projection = pyrr.matrix44.create_perspective_projection_matrix(
        45, 1280 / 720, 0.1, 100
    )
    chibi_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
    monkey_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([-4, 0, 0]))

    # eye, target, up
    view = pyrr.matrix44.create_look_at(
        pyrr.Vector3([0, 0, 8]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0])
    )

    model_loc = glGetUniformLocation(shader, "model")
    global proj_loc
    proj_loc = glGetUniformLocation(shader, "projection")
    view_loc = glGetUniformLocation(shader, "view")

    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

    model_01 = Model(
        chibi_indices, chibi_buffer, textures[0], chibi_pos, VAO[0], VBO[0]
    )
    model_02 = Model(
        monkey_indices, monkey_buffer, textures[1], monkey_pos, VAO[1], VBO[1]
    )

    animate(window, model_loc, [model_01, model_02])
    glfw.terminate()


main()
