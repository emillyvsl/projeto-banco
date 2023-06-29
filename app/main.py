import tkinter as tk
from adicionarCliente import AdicionarClientes
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca
from criarConta import CriarConta
from verClientes import VerClientes
from mostrarBanco import MostrarBanco
from atualizarBanco import AtualizarBanco
from cadastrarBanco import CadastrarBanco

class TelaPrincipal:
    def __init__(self, master):
        self._janela = master
        self._janela.title("Sistema Bancário")
        self._janela.geometry('500x500')

        mnu_barra = tk.Menu(self._janela)
        self._janela.config(menu=mnu_barra)

        mnu_banco = tk.Menu(mnu_barra)
        mnu_barra.add_cascade(label='Banco', menu=mnu_banco)
        mnu_banco.add_command(label='Cadastrar banco', command=self.abrir_cadastrar_banco)

        mnu_banco.add_command(label='Mostrar bancos', command=self.abrir_mostrar_banco)
        mnu_banco.add_command(label='Atualizar informações', command=self.abrir_atualizar_banco)

        mnu_cliente = tk.Menu(mnu_barra)
        mnu_barra.add_cascade(label='Cliente', menu=mnu_cliente)
        mnu_cliente.add_command(label='Ver clientes', command=self.abrir_ver_cliente)
        mnu_cliente.add_command(label='Adicionar clientes', command=self.abrir_adicionar_cliente)

        mnu_conta = tk.Menu(mnu_barra)
        mnu_barra.add_cascade(label='Conta', menu=mnu_conta)
        mnu_conta.add_command(label='Criar Conta', command=self.abrir_criar_conta)
        mnu_conta.add_command(label='Conta Corrente', command=self.abrir_conta_corrente)
        mnu_conta.add_command(label='Conta Poupança', command=self.abrir_conta_poupanca)

    #Funções para abrir as janelas
    def abrir_cadastrar_banco(self):
        cadastrar_banco = CadastrarBanco(self._janela)

    def abrir_atualizar_banco(self):
        atualizar_banco = AtualizarBanco(self._janela)

    def abrir_mostrar_banco(self):
        mostrar_banco = MostrarBanco(self._janela)
    
    def abrir_ver_cliente(self):
        ver_clientes = VerClientes(self._janela)

    def abrir_adicionar_cliente(self):
        adicinar_clientes = AdicionarClientes(self._janela)

    def abrir_criar_conta(self):
        criar_conta = CriarConta(self._janela)

    def abrir_conta_corrente(self):
        conta_corrente = ContaCorrente(self._janela)

    def abrir_conta_poupanca(self):
        conta_poupanca = ContaPoupanca(self._janela)

    #c

    

master = tk.Tk()
app = TelaPrincipal(master)
master.mainloop()
