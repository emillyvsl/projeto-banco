import datetime
from historico import Historico
from conta import Conta

x = datetime.datetime.now()

class ContaPoupanca(Conta):
    _contap = []

    def __init__(self, cli, banco, saldo=0):
        super().__init__(cli, saldo, banco)
        self.__taxa_juros = banco.jurosBanco
        self.addContaP()

    def atualizar_juros(self):
        juros = self.saldo * self.__taxa_juros
        self.saldo += juros

    def addContaP(self):
        self._contap.append(self)

    @classmethod
    def mostrarContasP(cls):
        return [conta for conta in cls._contap]

    def set_depositar(self, valor):
        if self.status:
            self.saldo += valor
            self._historico.incluir(f'Depósito de {valor}, data/hora:{x}')
            return True
        else:
            raise ValueError("A conta está desativada. O depósito não pode ser realizado.")

    def set_sacar(self, valor):
        if self.status:
            if valor <= self.saldo:
                self.saldo -= valor
                self._historico.incluir(f'Saque de {valor}, data/hora:{x}')
                self.saldo#chamando para atualizar o saldo atual no extrato
                return True
            else:
                return "sem saldo"
        else:
            return False
