from conta import Conta


class ContaCorrente(Conta):
    def __init__(self,cli,saldo,desconto,banco=None,):
        super.__init__(self,cli,saldo,banco)
        self.__desconto = desconto

    @property
    def deconto(self):
        return self.__desconto

    @deconto.setter
    def deconto(self, value):
        self.__desconto = value
        
    def depositar(self, valor):
        desco = valor * self.deconto
        valor -= desco
        self.saldo(valor)

    def sacar(self, valor):
        desconto = valor * self.desconto
        valor -= desconto
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")