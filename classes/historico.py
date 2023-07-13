class Hitorico:
    def __init__(self):
        self._listaObjetos= []


    @property
    def listas(self):
        return  self._listaObjetos

    @listas.setter
    def listas(self, value):
        self._listaObjetos.append(value)
