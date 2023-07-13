import tkinter as tk
import sys
from tkinter import ttk
from adicionarCliente import AdicionarClientes
sys.path.insert(0, './')
sys.path.insert(0, './classes')

from classes.cliente import Cliente

class VerClientes:
    def mostrarClientes(self):
        lista_cliente = Cliente.mostrarClientes()
        for cliente in lista_cliente:
            self.treeview.insert('', 'end', values=(cliente.numero, cliente.nome, cliente.cpf, cliente.endereco))

    


    def __init__(self, janela_anterior):
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(janela_anterior)
        self._janela.title("Lista de Clientes")
        self._janela.geometry('700x500')


        colunas = ('ID', 'Nome', 'Cpf', 'Endereço')

        self.treeview = ttk.Treeview(self._janela, columns=colunas, show='headings')
        self.treeview.grid(row=0, column=0, rowspan=5, padx=10, pady=10, sticky='nsew')

        # Configurar redimensionamento responsivo
        self._janela.grid_rowconfigure(0, weight=1)
        self._janela.grid_columnconfigure(0, weight=1)

      # Cabeçalhos
        for coluna in colunas:
            self.treeview.heading(coluna, text=coluna)

        # Colunas
        self.treeview.column('ID', minwidth=50, width=50)
        self.treeview.column('Nome', minwidth=200, width=200)
        self.treeview.column('Cpf', minwidth=200, width=200)
        self.treeview.column('Endereço', minwidth=200, width=200)

        
        # Barra de rolagem
        scb = ttk.Scrollbar(self._janela, orient=tk.VERTICAL, command=self.treeview.yview)
        scb.grid(row=0, column=1, rowspan=5, sticky='ns')
        self.treeview.config(yscrollcommand=scb.set)

        # Chamar a função para mostrar os bancos na tabela
        self.mostrarClientes()





        frame_btn = tk.Frame(self._janela)
        frame_btn.grid(row=5,column=0)
        
        btn_editar = tk.Button(frame_btn, text='Editar') #command=self.editar
        btn_editar.grid(row=5, column=0)

        btn_excluir = tk.Button(frame_btn, text='Excluir')#,command=self.excluir
        btn_excluir.grid(row=5,column=1)

        btn_incluir = tk.Button(frame_btn, text='Incluir', command=self.incluir_cliente)
        btn_incluir.grid(row=5, column=2)

        btn_pesq = tk.Button(frame_btn, text='Pesquisar')
        btn_pesq.grid(row=5,column=3)

        btn = tk.Button(frame_btn, text='Voltar', command=self.voltar)
        btn.grid(row=5, column=4)

    def incluir_cliente(self):
        AdicionarClientes(self._janela)
       
    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()