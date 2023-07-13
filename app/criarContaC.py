import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

sys.path.insert(0, './')
sys.path.insert(0, './classes')

from classes.cliente import Cliente
from classes.banco import Banco
from classes.contaCorrente import ContaCorrente


class CriarContaC:
    def __init__(self, janela_anterior, clientes, bancos):
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(janela_anterior)
        self._janela.title("Criar Conta Corrente")
        self._janela.geometry('500x500')
        


        lbl_Cliente = tk.Label(self._janela, text='Escolha um cliente: ')
        lbl_Cliente.grid(row=0, column=0)

      
        self.combobox_cliente = ttk.Combobox(self._janela, values=[i.nome for i in Cliente._clientes], state='readonly')
        self.combobox_cliente.grid(row=0, column=1)

        lbl_banco = tk.Label(self._janela, text='Escolha um banco: ')
        lbl_banco.grid(row=1, column=0)


        self.combobox_banco = ttk.Combobox(self._janela, values=[i.nome for i in Banco._bancos], state='readonly')
        self.combobox_banco.grid(row=1, column=1)

        self.lbl_contas_cadastradas = tk.Label(self._janela, text='Contas Cadastradas:')
        self.lbl_contas_cadastradas.grid(row=3, columnspan=2)

        btn_cadastrar = tk.Button(self._janela, text='Cadastrar', command=self.criar_conta_corrente)
        btn_cadastrar.grid(row=4, columnspan=2)

        btn_voltar = tk.Button(self._janela, text='Voltar', command=self.voltar)
        btn_voltar.grid(row=5, columnspan=2)

    def criar_conta_corrente(self):
        cliente_nome = self.combobox_cliente.get()
        banco_nome = self.combobox_banco.get()
        contaC = ContaCorrente(cliente_nome, banco_nome)
        messagebox.showinfo("Sucesso", "Conta corrente cadastrado com sucesso!")
        lbl_info = tk.Label(self._janela, text=f"ID: {contaC.numero}\nCliente: {contaC.titular}\nBanco: {contaC.banco}")
        lbl_info.grid(row=6, columnspan=2)
        


    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()




        
