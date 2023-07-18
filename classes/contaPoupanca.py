from conta import Conta

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
        


