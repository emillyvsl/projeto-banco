import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from app.criarContaC import CriarContaC
from banco import Banco
from cliente import Cliente

from sacar import Sacar
from depositar import Depositar
from mostrarExtrato import MostrarExtrato

import sys

sys.path.insert(0, './')
sys.path.insert(0, './classes')
from classes.contaCorrente import ContaCorrente


class ContaCorrenteI:
    def mostrarContas(self):
    

        lista_contaC = ContaCorrente.mostrarContasC()
        for contaC in lista_contaC:
            status = "Ativa" if contaC.status else "Encerrada"
            self.treeview.insert('', 'end', values=(contaC.numero, contaC.titular, contaC.banco, status))

    def __init__(self, janela_anterior, clientes, bancos):
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(janela_anterior)
        self._janela.title("Lista de Conta Corrente")
        self._janela.geometry('700x500')

        colunas = ('ID', 'Titular', 'Banco', 'Status')

        self.treeview = ttk.Treeview(self._janela, columns=colunas, show='headings')
        self.treeview.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nsew')

        # Configurar redimensionamento responsivo
        self._janela.grid_rowconfigure(0, weight=1)
        self._janela.grid_rowconfigure(1, weight=1)
        self._janela.grid_columnconfigure(0, weight=1)

        # Cabeçalhos
        for coluna in colunas:
            self.treeview.heading(coluna, text=coluna)

        # Colunas
        self.treeview.column('ID', minwidth=50, width=50)
        self.treeview.column('Titular', minwidth=200, width=200)
        self.treeview.column('Banco', minwidth=200, width=200)
        self.treeview.column('Status', minwidth=100, width=100)  # Coluna para mostrar o status

        # Barra de rolagem
        scb = ttk.Scrollbar(self._janela, orient=tk.VERTICAL, command=self.treeview.yview)
        scb.grid(row=0, column=1, rowspan=2, sticky='ns')
        self.treeview.config(yscrollcommand=scb.set)

        self.mostrarContas()

        btn_frame = tk.Frame(self._janela)
        btn_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        btn_depositar = tk.Button(btn_frame, text='Depositar', command=self.depositar)
        btn_depositar.pack(side='left', padx=5, pady=5, expand=True)

        btn_sacar = tk.Button(btn_frame, text='Sacar', command=self.sacar)
        btn_sacar.pack(side='left', padx=5, pady=5, expand=True)


        btn_incluir = tk.Button(btn_frame, text='Incluir', command=self.incluir)
        btn_incluir.pack(side='left', padx=5, pady=5, expand=True)

        btn_excluir = tk.Button(btn_frame, text='Excluir', command=self.excluir_conta_corrente)
        btn_excluir.pack(side='left', padx=5, pady=5, expand=True)

        btn_voltar = tk.Button(btn_frame, text='Voltar', command=self.voltar)
        btn_voltar.pack(side='left', padx=5, pady=5, expand=True)

        btn_historico = tk.Button(btn_frame, text='Extrato', command=self.historico)
        btn_historico.pack(side='left', padx=5, pady=5, expand=True)

        # Configurar redimensionamento responsivo para botões
        btn_frame.grid_columnconfigure(0, weight=1)

        self._janela.grid_rowconfigure(2, weight=1)
        self._janela.grid_columnconfigure(0, weight=1)

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()

    def depositar(self):
        item_selecionado = self.treeview.focus()
        if item_selecionado:
            valores = self.treeview.item(item_selecionado)['values']
            numero_conta = valores[0]
            conta_encontrada = None
            for conta in ContaCorrente.mostrarContasC():
                if conta.numero == numero_conta:
                    conta_encontrada = conta
                    break
            if conta_encontrada:
                if conta_encontrada.status:  # Verifica se a conta está ativa
                    self.janela_depositar = Depositar(self._janela, conta_encontrada)
                    self.janela_depositar.abrir_janela()
                else:
                    messagebox.showerror("Erro", "A conta está desativada e não pode ser usada.")
            else:
                messagebox.showerror("Erro", "Conta não encontrada.")

    def sacar(self):
        item_selecionado = self.treeview.focus()
        if item_selecionado:
            valores = self.treeview.item(item_selecionado)['values']
            numero_conta = valores[0]
            conta_encontrada = None
            for conta in ContaCorrente.mostrarContasC():
                if conta.numero == numero_conta:
                    conta_encontrada = conta
                    break
            if conta_encontrada:
                if conta_encontrada.status:  # Verifica se a conta está ativa
                    self.janela_sacar = Sacar(self._janela, conta_encontrada)
                    self.janela_sacar.abrir_janela()
                else:
                    messagebox.showerror("Erro", "A conta está desativada e não pode ser usada.")
            else:
                messagebox.showerror("Erro", "Conta não encontrada.")
    def historico(self):
        item_selecionado = self.treeview.focus()
        if item_selecionado:
            valores = self.treeview.item(item_selecionado)['values']
            numero_cliente = valores[0]
            cliente_encontrado = None
            for cliente in ContaCorrente.mostrarContasC():
                if cliente.numero == numero_cliente:
                    cliente_encontrado = cliente
                    break
            MostrarExtrato(self._janela, cliente_encontrado)

    def excluir_conta_corrente(self):
        item_selecionado = self.treeview.focus()
        if item_selecionado:
            valores = self.treeview.item(item_selecionado)['values']
            numero_conta = valores[0]
            conta_encontrada = None
            for conta in ContaCorrente.mostrarContasC():
                if conta.numero == numero_conta:
                    conta_encontrada = conta
                    break
            if conta_encontrada:
                if conta_encontrada.encerrarConta():
                    messagebox.showinfo("Sucesso", "Conta corrente excluída com sucesso!")
                    # Atualizar a tabela após a exclusão
                    self.treeview.delete(*self.treeview.get_children())  # Limpa a tabela
                    self.mostrarContas()  # Reinsere as contas na tabela
                else:
                    messagebox.showerror("Erro", "Não é possível excluir a conta. Verifique se o saldo é zero.")
            else:
                messagebox.showerror("Erro", "Conta não encontrada.")

    def incluir(self):
        # Abrir a janela de criar conta corrente
        self.janela_criar_conta_corrente = CriarContaC(self._janela, Cliente._clientes, Banco._lista)  # Passe os clientes e bancos como argumentos
        
        # Aguardar até que a janela de criação seja destruída (após a inclusão ser confirmada)
        self._janela.wait_window(self.janela_criar_conta_corrente._janela)

        # Atualizar a tabela após a inclusão
        self.treeview.delete(*self.treeview.get_children())  # Limpa a tabela
        self.mostrarContas()  # Reinsere as contas na tabela