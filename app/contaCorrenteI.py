import tkinter as tk
from tkinter import ttk
from contaCorrente import ContaCorrente
from criarContaC import CriarContaC


class ContaCorrenteI:
    def mostrarContas(self):
        lista_contaC = ContaCorrente.mostrarContas()
        for contaC in lista_contaC:
            self.treeview.insert('', 'end', values=(contaC.numero, contaC.titular, contaC.banco))

    def __init__(self, janela_anterior):
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(janela_anterior)
        self._janela.title("Conta Corrente")
        self._janela.geometry('500x500')

        colunas = ('ID', 'Titular', 'Banco')

        self.treeview = ttk.Treeview(self._janela, columns=colunas, show='headings')
        self.treeview.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        # Configurar redimensionamento responsivo
        self._janela.grid_rowconfigure(0, weight=1)
        self._janela.grid_columnconfigure(0, weight=1)

        # Cabeçalhos
        for coluna in colunas:
            self.treeview.heading(coluna, text=coluna)

        # Colunas
        self.treeview.column('ID', minwidth=50, width=50)
        self.treeview.column('Titular', minwidth=200, width=200)
        self.treeview.column('Banco', minwidth=200, width=200)

        # Barra de rolagem
        scb = ttk.Scrollbar(self._janela, orient=tk.VERTICAL, command=self.treeview.yview)
        scb.grid(row=0, column=1, sticky='ns')
        self.treeview.config(yscrollcommand=scb.set)

        self.mostrarContas()

        btn_frame = tk.Frame(self._janela)
        btn_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky='nsew')

        btn_depositar = tk.Button(btn_frame, text='Depositar')
        btn_depositar.pack(side='left', padx=5, pady=5, expand=True)

        btn_sacar = tk.Button(btn_frame, text='Sacar')
        btn_sacar.pack(side='left', padx=5, pady=5, expand=True)

        btn_listar = tk.Button(btn_frame, text='Listar Contas', command=self.mostrarContas)
        btn_listar.pack(side='left', padx=5, pady=5, expand=True)

        btn_incluir = tk.Button(btn_frame, text='Incluir')
        btn_incluir.pack(side='left', padx=5, pady=5, expand=True)

        btn_excluir = tk.Button(btn_frame, text='Excluir')
        btn_excluir.pack(side='left', padx=5, pady=5, expand=True)

        btn_voltar = tk.Button(btn_frame, text='Voltar', command=self.voltar)
        btn_voltar.pack(side='left', padx=5, pady=5, expand=True)

        # Configurar redimensionamento responsivo para botões
        btn_frame.grid_columnconfigure(0, weight=1)

        self._janela.grid_rowconfigure(1, weight=1)
        self._janela.grid_columnconfigure(0, weight=1)

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()
