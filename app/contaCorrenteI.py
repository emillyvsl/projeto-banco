import tkinter as tk
from tkinter import ttk
from contaCorrente import ContaCorrente

class ContaCorrenteI:
    def mostrarContas(self):
        # Obter todas as contas correntes cadastradas
        self.contas_cadastradas = ContaCorrente.mostrarContas()

        # Preencher a tabela com todas as contas correntes cadastradas
        for conta in self.contas_cadastradas:
            cliente_nome = conta.cliente_nome
            banco = conta.banco.nome
            self.treeview.insert('', 'end', values=(cliente_nome, banco))

    def __init__(self, janela_anterior):
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(janela_anterior)
        self._janela.title("Conta Corrente")
        self._janela.geometry('500x500')

        self.treeview = ttk.Treeview(self._janela, columns=('cliente', 'banco'), show='headings')
        self.treeview.heading('cliente', text='Cliente')
        self.treeview.heading('banco', text='Banco')
        self.treeview.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky='nsew')

        self.scrollbar = ttk.Scrollbar(self._janela, orient='vertical', command=self.treeview.yview)
        self.scrollbar.grid(row=0, column=6, sticky='ns')
        self.treeview.configure(yscrollcommand=self.scrollbar.set)

        btn_depositar = tk.Button(self._janela, text='Depositar')
        btn_depositar.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

        btn_sacar = tk.Button(self._janela, text='Sacar')
        btn_sacar.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

        btn_listar = tk.Button(self._janela, text='Listar Contas', command=self.mostrarContas)
        btn_listar.grid(row=1, column=2, padx=5, pady=5, sticky='nsew')

        btn_incluir = tk.Button(self._janela, text='Incluir')
        btn_incluir.grid(row=1, column=3, padx=5, pady=5, sticky='nsew')

        btn_excluir = tk.Button(self._janela, text='Excluir')
        btn_excluir.grid(row=1, column=4, padx=5, pady=5, sticky='nsew')

        btn_voltar = tk.Button(self._janela, text='Voltar', command=self.voltar)
        btn_voltar.grid(row=1, column=5, padx=5, pady=5, sticky='nsew')

        self.contas_cadastradas = []  # Lista para armazenar as contas cadastradas

        self._janela.grid_rowconfigure(0, weight=1)
        self._janela.grid_columnconfigure(0, weight=1)

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()
