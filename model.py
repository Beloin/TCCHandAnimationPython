import pyrr
from ObjLoader import ObjLoader
from OpenGL.GL import *
from TextureLoader import load_texture

class Model:
    def __init__(self, indices, buffer, textures, pos, VAO, VBO) -> None:
        self._indices = indices
        self._buffer = buffer
        self._textures = textures
        self._vao = VAO
        self._vbo = VBO
        self._pos = pos

    def get_indices(self):
        return self._indices

    def get_buffer(self):
        return self._buffer

    def get_pos(self):
        return self._pos

    def get_VAO(self):
        return self._vao

    def get_VBO(self):
        return self._vbo

    def get_texture(self):
        return self._textures


def create_model(filename: str, texture_f: str, pos=None) -> Model:
    model_indices, model_buffer = ObjLoader.load_model(filename)
    model_vao = glGenVertexArrays(1)
    model_vbo = glGenBuffers(1)

    glBindVertexArray(model_vao)
    glBindBuffer(GL_ARRAY_BUFFER, model_vbo)
    glBufferData(GL_ARRAY_BUFFER, model_buffer.nbytes, model_buffer, GL_STATIC_DRAW)

    # Model vertices
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(
        0, 3, GL_FLOAT, GL_FALSE, model_buffer.itemsize * 8, ctypes.c_void_p(0)
    )
    # Model textures
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(
        1, 2, GL_FLOAT, GL_FALSE, model_buffer.itemsize * 8, ctypes.c_void_p(12)
    )
    # Model normals
    glVertexAttribPointer(
        2, 3, GL_FLOAT, GL_FALSE, model_buffer.itemsize * 8, ctypes.c_void_p(20)
    )
    glEnableVertexAttribArray(2)

    textures = glGenTextures(1)
    load_texture(texture_f, textures)

    model_pos = pos if pos is not None else pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))

    return Model(model_indices, model_buffer, textures, model_pos, model_vao, model_vbo)

