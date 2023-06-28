class Conta:
    _id =0
    def __init__(self, cli, sal,banco=None):
        self.__numero = self.num()
        self.__banco = banco
        self.__titular = cli
        self.__saldo = sal
#Métodos

    @classmethod
    def num(cls):
        cls._id +=1
        return cls._id

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, value):
        self.__titular = value

    @property
    def saldo(self):
        return self.__saldo

    def set_depositar(self,value):
        self.__saldo = value

    def set_sacar(self,value):
        self.__saldo -= value

    @property
    def banco(self):
        if self.__banco != None:
            return self.__banco
