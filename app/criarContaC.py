import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

sys.path.insert(0, './')
sys.path.insert(0, './classes')

from classes.cliente import Cliente
from classes.contaCorrente import ContaCorrente


class CriarContaC:
    def __init__(self, janela_anterior, clientes, bancos):
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(janela_anterior)
        self._janela.title("Criar Conta Corrente")
        self._janela.geometry('500x500')

        self.clientes = clientes
        self.bancos = bancos

        lbl_Cliente = tk.Label(self._janela, text='Escolha um cliente: ')
        lbl_Cliente.grid(row=0, column=0)

        # Criar lista com os nomes dos clientes cadastrados
        nomes_clientes = [cliente.nome for cliente in clientes]

        self.combobox_cliente = ttk.Combobox(self._janela, values=nomes_clientes, state='readonly')
        self.combobox_cliente.grid(row=0, column=1)

        lbl_banco = tk.Label(self._janela, text='Escolha um banco: ')
        lbl_banco.grid(row=1, column=0)

        # Criar lista com os nomes dos bancos cadastrados
        nomes_bancos = [banco.nome for banco in bancos]

        self.combobox_banco = ttk.Combobox(self._janela, values=nomes_bancos, state='readonly')
        self.combobox_banco.grid(row=1, column=1)

        #lbl_saldo = tk.Label(self._janela, text='Saldo: ')
        #lbl_saldo.grid(row=2, column=0)

        #self.ent_saldo = tk.Entry(self._janela)
        #self.ent_saldo.grid(row=2, column=1)

        self.lbl_contas_cadastradas = tk.Label(self._janela, text='Contas Cadastradas:')
        self.lbl_contas_cadastradas.grid(row=3, columnspan=2)

        btn_cadastrar = tk.Button(self._janela, text='Cadastrar', command=self.criar_conta_corrente)
        btn_cadastrar.grid(row=4, columnspan=2)

        btn_voltar = tk.Button(self._janela, text='Voltar', command=self.voltar)
        btn_voltar.grid(row=5, columnspan=2)

        self.contas_cadastradas = []  # Lista para armazenar as contas cadastradas

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()

    def criar_conta_corrente(self):
        cliente_nome = self.combobox_cliente.get()
        banco_nome = self.combobox_banco.get()
        #saldo = float(self.ent_saldo.get())

        cliente = None
        banco = None

        # Procura o objeto Cliente correspondente ao nome selecionado
        for cli in self.clientes:
            if cli.nome == cliente_nome:
                cliente = cli
                break

        # Procura o objeto Banco correspondente ao nome selecionado
        for ban in self.bancos:
            if ban.nome == banco_nome:
                banco = ban
                break

        if cliente is None or banco is None:
            messagebox.showerror("Erro", "Cliente ou banco não encontrado.")
            return

        conta_corrente = ContaCorrente(cliente, banco)
        self.contas_cadastradas.append(conta_corrente)

        # Exibe as informações da conta cadastrada na label
        lbl_conta_cadastrada = tk.Label(self._janela, text=f"Conta Cadastrada:\nCliente: {cliente.nome} | Saldo: {saldo}")
        lbl_conta_cadastrada.grid(row=6, columnspan=2)

        messagebox.showinfo("Sucesso", "Conta corrente criada com sucesso!")
        self.voltar()
