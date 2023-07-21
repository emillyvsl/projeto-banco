from conta import Conta
import datetime

x = datetime.datetime.now()

class ContaCorrente(Conta):
    _contaC = []
    def __init__(self, cli, banco, saldo=0):
        super().__init__(cli, saldo, banco)
        self.__desconto = 0.05
        self.addContaC()

    @property
    def desconto(self):
        return self.__desconto

    @desconto.setter
    def desconto(self, value):

        self.__desconto = value

    def set_depositar(self, valor):
        desconto = valor * self.desconto
        valor -= desconto
        if self.status:
            self.saldo += valor
            self._historico.incluir(f'Deposito de {valor}, data/hora:{x}')
            return True
        else:
            raise ValueError("A conta está desativada. O depósito não pode ser realizado.")


    def set_sacar(self, valor):
        desconto = valor * self.desconto
        valor -= desconto
        if self.status:
            if valor <= self.saldo:
                self.saldo -= valor
                self._historico.incluir(f'Saque de {valor}, data/hora:{x}')
                return True
            else:
                return "sem saldo"
        else:
            return False
        
    def addContaC(self):
        self._contaC.append(self)

    @classmethod
    def mostrarContasC(cls):
        return [conta for conta in cls._contaC]
