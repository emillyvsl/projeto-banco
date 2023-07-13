import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

sys.path.insert(0, './')
sys.path.insert(0, './classes')

from classes.cliente import Cliente
from classes.banco import Banco
from classes.contaPoupanca import ContaPoupanca


class CriarContaP:
    def __init__(self, janela_anterior, clientes, bancos):
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(janela_anterior)
        self._janela.title("Criar Conta Corrente")
        self._janela.geometry('700x500')
        


        lbl_Cliente = tk.Label(self._janela, text='Escolha um cliente: ')
        lbl_Cliente.grid(row=0, column=0, sticky='w', padx=10, pady=5)

        self.combobox_cliente = ttk.Combobox(self._janela, values=[i.nome for i in Cliente._clientes], state='readonly')
        self.combobox_cliente.grid(row=0, column=1, sticky='e', padx=10, pady=5)

        lbl_banco = tk.Label(self._janela, text='Escolha um banco: ')
        lbl_banco.grid(row=1, column=0, sticky='w', padx=10, pady=5)

        self.combobox_banco = ttk.Combobox(self._janela, values=[i.nome for i in Banco._lista], state='readonly')
        self.combobox_banco.grid(row=1, column=1, sticky='e', padx=10, pady=5)

        btn_frame = tk.Frame(self._janela)
        btn_frame.grid(row=4, columnspan=2, padx=10, pady=10)

        btn_cadastrar = tk.Button(btn_frame, text='Cadastrar', command=self.criar_conta_poupanca)
        btn_cadastrar.pack(side='left', padx=5)

        btn_voltar = tk.Button(btn_frame, text='Voltar', command=self.voltar)
        btn_voltar.pack(side='left', padx=5)

    def criar_conta_poupanca(self):
        cliente_nome = self.combobox_cliente.get()
        banco_nome = self.combobox_banco.get()

        if not banco_nome:
            messagebox.showerror("Erro", "Selecione um banco.")
            return
        
        if not cliente_nome:
            messagebox.showerror("Erro", "Selecione um cliente.")
            return

        banco_selecionado = None
        for banco in Banco._lista:
            if banco.nome == banco_nome:
                banco_selecionado = banco
                break

        if banco_selecionado is None:
            messagebox.showerror("Erro", "Banco selecionado inválido.")
            return

        contaP = ContaPoupanca(cliente_nome, banco_selecionado)
        messagebox.showinfo("Sucesso", "Conta poupança cadastrada com sucesso!")
        lbl_info = tk.Label(self._janela, text=f"ID: {contaP.numero}\nCliente: {contaP.titular}\nBanco: {contaP.banco}")
        lbl_info.grid(row=6, columnspan=2)

        


    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()




        
