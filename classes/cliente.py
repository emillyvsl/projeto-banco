
from historico import Historico
class Cliente:
    _id = 0
    _clientes = []
    def __init__(self, n, cpf, e):
        self.__num = self.num()
        self.__nome = n
        self.__endereco = e
        self.__CPF = cpf
        self.incluirCliente()
        self._status = True

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
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, value):
        self.__endereco = value

    @property
    def cpf(self):
        return self.__CPF

    @cpf.setter
    def cpf(self, value):
        self.__CPF = value

    def incluirCliente(self):
        Cliente._clientes.append(self)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @classmethod
    def removerCliente(cls, cliente):
        if cliente in Cliente._clientes:
            Cliente._clientes.remove(cliente)#remove da lista
            return True
        else:
            return False


    @classmethod
    def mostrarClientes(cls):
        return [i for i in Cliente._clientes if i.status == True]#so ira retornar as contas ativadas
