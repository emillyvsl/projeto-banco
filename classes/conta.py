class Conta:
    _id = 0
    _contas = []

    def __init__(self, cli, sal=0, banco=None):
        self.__numero = self.num()
        self.__banco = banco
        self.__titular = cli
        self.__saldo = sal
        self._status = True
        self.incluirConta()

    @classmethod
    def num(cls):
        cls._id += 1
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def saldo(self):
        if self.status:
            return self.__saldo

    def set_depositar(self, value):
        if self.status:
            self.__saldo = value
        else:
            return False  # Significa que a conta está desativada

    def set_sacar(self, value):
        if self.status:
            if value <= self.saldo:
                self.__saldo -= value
                return True  # Se o saque for bem-sucedido, retorna verdadeiro
            else:
                return False  # Se for falso, significa que não há saldo suficiente
        else:
            return False  # Significa que a conta não está ativa

    @property
    def banco(self):
        if self.__banco is not None:
            return self.__banco

    def incluirConta(self):
        # Deve ser chamado somente ao criar um novo objeto
        self._contas.append(self)

    @classmethod
    def mostrarContas(cls):
        # Retorna uma lista dos objetos conta
        return [i.titular for i in cls._contas]
