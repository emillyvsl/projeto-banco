import tkinter as tk
from tkinter import messagebox
from adicionarCliente import AdicionarClientes
from minhaConta import MinhaConta
from contaPoupancaI import ContaPoupancaI
from criarContaP import CriarContaP
from contaCorrenteI import ContaCorrenteI
from contaPoupanca import ContaPoupanca
from criarContaC import CriarContaC
from verClientes import VerClientes
from mostrarBanco import MostrarBanco
from atualizarBanco import AtualizarBanco
from cadastrarBanco import CadastrarBanco
import sys
from tkinter import ttk
from PIL import Image, ImageTk
#pode ser necessario instalar para usar a imagem 
#pip install pillow



sys.path.insert(0, './')
sys.path.insert(0, './banco')
sys.path.insert(0, './classes')
from classes.banco import Banco
from classes.cliente import Cliente

class TelaPrincipal:
    def __init__(self, master):
        self._janela = master
        self._janela.title("Sistema Bancário")
        self._janela.geometry('500x500')

        
        self.adicionar_clientes = None  # Inicializa o atributo como None
        self.adicionar_banco = None  # Inicializa o atributo como None

        mnu_barra = tk.Menu(self._janela)
        self._janela.config(menu=mnu_barra)

        mnu_banco = tk.Menu(mnu_barra)
        mnu_barra.add_cascade(label='Banco', menu=mnu_banco)
        mnu_banco.add_command(label='Cadastrar banco', command=self.abrir_cadastrar_banco)
        mnu_banco.add_command(label='Mostrar bancos', command=self.abrir_mostrar_banco)
        mnu_banco.add_command(label='Atualizar informações', command=self.abrir_atualizar_banco)

        mnu_cliente = tk.Menu(mnu_barra)
        mnu_barra.add_cascade(label='Cliente', menu=mnu_cliente)
        mnu_cliente.add_command(label='Adicionar clientes', command=self.abrir_adicionar_cliente)
        mnu_cliente.add_command(label='Ver clientes', command=self.abrir_ver_cliente)

        mnu_conta = tk.Menu(mnu_barra)
        mnu_barra.add_cascade(label='Conta', menu=mnu_conta)

        submenu_criar_conta = tk.Menu(mnu_conta)
        mnu_conta.add_cascade(label='Criar Conta', menu=submenu_criar_conta)
        submenu_criar_conta.add_command(label='Conta Corrente', command=self.abrir_criar_contaC)
        submenu_criar_conta.add_command(label='Conta Poupança', command=self.abrir_criar_contaP)

        mnu_conta.add_command(label='Conta Corrente', command=self.abrir_conta_corrente)
        mnu_conta.add_command(label='Conta Poupança', command=self.abrir_conta_poupanca)
        mnu_conta.add_command(label='Minha conta',command=self.contas)
    
        # Carregar e exibir a imagem
        imagem = Image.open(r"C:\Users\sthef\OneDrive\Documentos\GitHub\Projeto-Banco\app\banco.png")

        imagem = imagem.resize((300, 300))  # Redimensionar a imagem conforme necessário
        self.minha_imagem = ImageTk.PhotoImage(imagem)

        frame_imagem = ttk.Frame(self._janela)
        frame_imagem.pack(pady=100, anchor='s')

        label_imagem = ttk.Label(frame_imagem, image=self.minha_imagem)
        label_imagem.pack()
    
    # Funções para abrir as janelas
    def abrir_cadastrar_banco(self):
        self.adicionar_banco = CadastrarBanco(self._janela)

    def abrir_atualizar_banco(self):
        AtualizarBanco(self._janela)

    def abrir_mostrar_banco(self):
        MostrarBanco(self._janela)

    def abrir_ver_cliente(self):
        VerClientes(self._janela)

    def abrir_adicionar_cliente(self):
        self.adicionar_clientes = AdicionarClientes(self._janela)

    def abrir_criar_contaC(self):
        if self.adicionar_clientes:
            if self.adicionar_banco:
                CriarContaC(self._janela, Banco._lista, Cliente._clientes)
            else:
                tk.messagebox.showerror("Erro", "Adicione um banco primeiro.")
        else:
            tk.messagebox.showerror("Erro", "Adicione clientes primeiro.")

    def abrir_criar_contaP(self):
        if self.adicionar_clientes:
            if self.adicionar_banco:
                CriarContaP(self._janela, Banco._lista, Cliente._clientes)
            else:
                tk.messagebox.showerror("Erro", "Adicione um banco primeiro.")
        else:
            tk.messagebox.showerror("Erro", "Adicione clientes primeiro.")

    def abrir_conta_corrente(self):
        ContaCorrenteI(self._janela)

    def abrir_conta_poupanca(self):
        ContaPoupancaI(self._janela, Banco.mostrarBancos())

    def contas(self):
        MinhaConta(self._janela)



def main():
    master = tk.Tk()
    app = TelaPrincipal(master)
    master.mainloop()


if __name__ == '__main__':
    main()
