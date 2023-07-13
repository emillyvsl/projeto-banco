from historico import Historico
class Banco:
    _id = 0

    def __init__(self, nome):
        self.__num = self.num()
        self.__nome = nome
        self.__contas = []
        self.incluirBancos()
        self.__jurosBanco = 0.3
        self.__historico = Historico()

    # métodos
    @classmethod
    def num(cls):
        cls._id += 1
        return cls._id

    @property
    def numero(self):
        return self.__num

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def listaContas(self):
        return self.__contas

    @listaContas.setter
    def listaContas(self, value):
        self.__contas.append(value)

    def incluirBancos(self):
        self.__historico.listas(self)

    @classmethod
    def mostrarBancos(self):
        return self.__h

    @property
    def jurosBanco(self):
        return self.__jurosBanco

    @jurosBanco.setter
    def jurosBanco(self, value):
        self.jurosBanco = value