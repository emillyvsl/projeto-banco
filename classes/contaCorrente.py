from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, cli, saldo, desconto, banco=None):
        super().__init__(cli, saldo, banco)
        self.__desconto = desconto

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
            self.saldo = valor
        else:
            return False  # Significa que a conta está desativada

    def set_sacar(self, valor):
        desconto = valor * self.desconto
        valor -= desconto
        if self.status:
            if valor <= self.saldo:
                self.saldo -= valor
                return True
            else:
                return False
        else:
            return False
