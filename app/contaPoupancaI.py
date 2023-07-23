import tkinter as tk
from tkinter import ttk

import sys
from tkinter import messagebox
from app.depositarC import Depositar
from app.mostrarExtrato import MostrarExtrato
from app.sacarC import Sacar

from cliente import Cliente

sys.path.insert(0, './')
sys.path.insert(0, './classes')
from classes.contaPoupanca import ContaPoupanca
from criarContaP import CriarContaP
from classes.banco import Banco  # Importe a classe Banco

class ContaPoupancaI:
    def mostrarContas(self):
        lista_contaP = ContaPoupanca.mostrarContasP()
        for contaP in lista_contaP:
            status = "Ativa" if contaP.status else "Encerrada"
            self.treeview.insert('', 'end', values=(contaP.numero, contaP.titular, contaP.banco.nome, status))

    def __init__(self, janela_anterior, bancos):  # Adicione o argumento bancos
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(janela_anterior)
        self._janela.title("Lista de Conta Poupança")
        self._janela.geometry('700x500')

        colunas = ('ID', 'Titular', 'Banco', 'Status')  # Adicione a coluna 'Status'

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

        btn_depositar = tk.Button(btn_frame, text='Depositar',command=self.depositar)
        btn_depositar.pack(side='left', padx=5, pady=5, expand=True)

        btn_sacar = tk.Button(btn_frame, text='Sacar',command=self.sacar)
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


    def incluir(self):
        CriarContaP(self._janela, Cliente.mostrarClientes(), Banco.mostrarBancos())  

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()
    def historico(self):
        item_selecionado = self.treeview.focus()
        if item_selecionado:
            valores = self.treeview.item(item_selecionado)['values']
            numero_cliente = valores[0]
            cliente_encontrado = None
            for cliente in ContaPoupanca.mostrarContasP():
                if cliente.numero == numero_cliente:
                    cliente_encontrado = cliente
                    break
            MostrarExtrato(self._janela,cliente_encontrado)
        
  


    def depositar(self):
        item_selecionado = self.treeview.focus()
        if item_selecionado:
            valores = self.treeview.item(item_selecionado)['values']
            numero_conta = valores[0]
            conta_encontrada = None
            for conta in ContaPoupanca.mostrarContasP():
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
            for conta in ContaPoupanca.mostrarContasP():
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

    def excluir_conta_corrente(self):
        item_selecionado = self.treeview.focus()
        if item_selecionado:
            valores = self.treeview.item(item_selecionado)['values']
            numero_conta = valores[0]
            conta_encontrada = None
            for conta in ContaPoupanca.mostrarContasP():
                if conta.numero == numero_conta:
                    conta_encontrada = conta
                    break
            if conta_encontrada:
                if conta_encontrada.encerrarConta():
                    messagebox.showinfo("Sucesso", "Conta corrente excluída com sucesso!")
                    self._janela.destroy()  # Fecha a janela de cadastro
                    self.janela_anterior.deiconify()  # Exibe a janela anterior
                    self.mostrarContas()  # Atualiza a lista de contas após a exclusão
                else:
                    messagebox.showerror("Erro", "Não é possível excluir a conta. Verifique se o saldo é zero.")
            else:
                messagebox.showerror("Erro", "Conta não encontrada.")

    def incluir(self):
        # Abrir a janela de criar conta corrente
        self.janela_criar_conta_corrente = CriarContaP(self._janela, Cliente._clientes, Banco._lista)  # Passe os clientes e bancos como argumentos
        


  

            