import datetime
from historico import Historico
x = datetime.datetime.now()
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
        Historico.adicionar_conta(self)
        self._historico = Historico()


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
            self._historico.incluir(f'Saldo atual:{self.__saldo} dia:{x}')
            return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if self.status:
            self.__saldo = value

    def set_depositar(self, valor):
        if self.status:
            self.saldo = valor
            self._historico.incluir(f'Deposito de {valor},data/hora:{x}')
        else:
            return False  # Significa que a conta está desativada

    # def set_sacar(self, value):
    #     if self.status:
    #         if value <= self.saldo:
    #             self.__saldo -= value
    #             return True  # Se o saque for bem-sucedido, retorna verdadeiro
    #         else:
    #             return False  # Se for falso, significa que não há saldo suficiente
    #     else:
    #         return False  # Significa que a conta não está ativa
    def set_sacar(self, valor):
        if self.status:
            if valor <= self.saldo:
                self.saldo -= valor
                self._historico.incluir(f'Saque de {valor},data/hora:{x}')
                return True
            else:
                return "sem saldo" # se esse for o retorno significa que não ha saldo suficiente
        else:
            return False

    @property
    def banco(self):
        if self.__banco is not None:
            return self.__banco

    def incluirConta(self):
        # Deve ser chamado somente ao criar um novo objeto
        self._contas.append(self)

    @classmethod
    def mostrarContas(cls):
        return [conta for conta in cls._contas]

    @property
    def clientes(self):
        return self.titular.mostrarClientes()

    def encerrarConta(self):
        if self.saldo == 0:  # Verifica se a conta possui saldo zero para poder ser encerrada
            self.status = False
            self._historico.incluir(f'Conta do(a) senhor(a) {self.titular} foi encerrada em {x}.')
            return True
        else:
            return False  # A conta não pode ser encerrada pois possui saldo
        
    def extrato(self):
        return self._historico.mostrar()





