from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, cli, banco, saldo=0):
        super().__init__(cli, saldo, banco)
        self.__taxa_juros = banco.jurosBanco

    def atualizar_juros(self):
        juros = self.saldo * self.__taxa_juros
        self.saldo += juros

