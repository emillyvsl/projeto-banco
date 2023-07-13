class Historico:
    contas_criadas = []

    @classmethod
    def adicionar_conta(cls, conta):
        cls.contas_criadas.append(conta)

    @classmethod
    def listar_contas(cls):
        return cls.contas_criadas
