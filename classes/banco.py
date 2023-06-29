class Banco:
    _id = 0

    def __init__(self, nome):
        self.__num = self.num()
        self.__nome = nome
        self.__contas = []
        

#metodos
    @classmethod
    def num(cls):
        cls._id +=1
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

