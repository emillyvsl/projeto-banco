class Historico:
    contas_criadas = []
    def __init__(self):
        self._relatorio= []
        
    #metodo para listar todas as contas independente do banco
    @classmethod
    def adicionar_conta(cls, conta):
        cls.contas_criadas.append(conta)

    @classmethod
    def listar_contas(cls):
        return cls.contas_criadas
    
    #relatorios/extrato, salva as operações feitas
    # nas contas, cada conta possuiu seu historico independente de estar ativada ou não
    def incluir(self,value):
        self._relatorio.append(value)
        
    def mostrar(self):
        return [i for i in self._relatorio]




