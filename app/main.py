import tkinter as tk
from adicionarCliente import AdicionarClientes
from contaCorrenteI import ContaCorrenteI
from contaPoupanca import ContaPoupanca
from criarContaC import CriarContaC
from verClientes import VerClientes
from mostrarBanco import MostrarBanco
from atualizarBanco import AtualizarBanco

from cadastrarBanco import CadastrarBanco

import sys
sys.path.insert(0, './')
sys.path.insert(0, './banco')
sys.path.insert(0, './classes')
from classes.banco import Banco

class TelaPrincipal:
    def __init__(self, master):
        
        self._janela = master
        self._janela.title("Sistema Bancário")
        self._janela.geometry('500x500')

         # Trocar a cor de fundo da janela
        #self._janela.configure(background='PaleTurquoise') 

       

        mnu_barra = tk.Menu(self._janela)
        self._janela.config(menu=mnu_barra)

        mnu_banco = tk.Menu(mnu_barra) 
        mnu_barra.add_cascade(label='Banco', menu=mnu_banco)
        mnu_banco.add_command(
            label='Cadastrar banco', command=self.abrir_cadastrar_banco)

        mnu_banco.add_command(
            label='Mostrar bancos', command=self.abrir_mostrar_banco)
        mnu_banco.add_command(label='Atualizar informações', command=self.abrir_atualizar_banco)

        mnu_cliente = tk.Menu(mnu_barra)
        mnu_barra.add_cascade(label='Cliente', menu=mnu_cliente)
        mnu_cliente.add_command(label='Adicionar clientes', command=self.abrir_adicionar_cliente)
        mnu_cliente.add_command(label='Ver clientes', command=self.abrir_ver_cliente)

        mnu_conta = tk.Menu(mnu_barra)
        mnu_barra.add_cascade(label='Conta', menu=mnu_conta)
        

        submenu_criar_conta = tk.Menu(mnu_conta)
        mnu_conta.add_cascade(label='Criar Conta', menu=submenu_criar_conta)

        # Adicionar as opções do submenu "Criar Conta"
        submenu_criar_conta.add_command(label='Conta Corrente', command=self.abrir_criar_contaC)
        submenu_criar_conta.add_command(label='Conta Poupança')


        mnu_conta.add_command(label='Conta Corrente', command=self.abrir_conta_corrente)
        mnu_conta.add_command(label='Conta Poupança', command=self.abrir_conta_poupanca)

    # Funções para abrir as janelas
    def abrir_cadastrar_banco(self):
        CadastrarBanco(self._janela)

    def abrir_atualizar_banco(self):
        AtualizarBanco(self._janela)

    def abrir_mostrar_banco(self):
        MostrarBanco(self._janela)
    
    def abrir_ver_cliente(self):
        VerClientes(self._janela)

    def abrir_adicionar_cliente(self):
        AdicionarClientes(self._janela)

    def abrir_criar_contaC(self):
        CriarContaC(self._janela)

    def abrir_conta_corrente(self):
        ContaCorrenteI(self._janela)

    def abrir_conta_poupanca(self):
        ContaPoupanca(self._janela)


def main():    
    master = tk.Tk()
    app = TelaPrincipal(master)
    master.mainloop()


if __name__ == '__main__':
    main()
