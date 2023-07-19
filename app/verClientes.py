import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
from adicionarCliente import AdicionarClientes
from editarCliente import EditarCliente
sys.path.insert(0, './')
sys.path.insert(0, './classes')

from classes.cliente import Cliente


class VerClientes:
    def mostrarClientes(self):
        lista_cliente = Cliente.mostrarClientes()
        for cliente in lista_cliente:
            self.treeview.insert('', 'end', values=(cliente.numero, cliente.nome, cliente.endereco, cliente.cpf))

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

        # Chamar a função para mostrar os clientes na tabela
        self.mostrarClientes()

        frame_btn = tk.Frame(self._janela)
        frame_btn.grid(row=5, column=0)

        btn_editar = tk.Button(frame_btn, text='Editar', command=self.editar_cliente)
        btn_editar.grid(row=5, column=0)

        btn_excluir = tk.Button(frame_btn, text='Excluir', command=self.excluir_cliente)
        btn_excluir.grid(row=5, column=1)

        btn_incluir = tk.Button(frame_btn, text='Incluir', command=self.incluir_cliente)
        btn_incluir.grid(row=5, column=2)

        # btn_pesq = tk.Button(frame_btn, text='Pesquisar')
        # btn_pesq.grid(row=5, column=3) 

        btn = tk.Button(frame_btn, text='Voltar', command=self.voltar)
        btn.grid(row=5, column=3)

    def editar_cliente(self):
        # Obter o item selecionado na treeview
        item_selecionado = self.treeview.focus()
        if item_selecionado:
            valores = self.treeview.item(item_selecionado)['values']
            numero_cliente = valores[0]
            cliente_encontrado = None
            for cliente in Cliente.mostrarClientes():
                if cliente.numero == numero_cliente:
                    cliente_encontrado = cliente
                    break
            if cliente_encontrado:
                # Abrir a janela de edição do cliente
                EditarCliente(cliente_encontrado)
            else:
                messagebox.showerror("Erro", "Cliente não encontrado.")

    def excluir_cliente(self):
        # Obter o item selecionado na treeview
        item_selecionado = self.treeview.focus()
        if item_selecionado:
            valores = self.treeview.item(item_selecionado)['values']
            numero_cliente = valores[0]
            cliente_encontrado = None
            for cliente in Cliente.mostrarClientes():
                if cliente.numero == numero_cliente:
                    cliente_encontrado = cliente
                    break
            if cliente_encontrado:
                # Excluir o cliente
                sucesso = Cliente.removerCliente(cliente_encontrado)
                if sucesso:
                    messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
                    # Remover o item da treeview
                    self.treeview.delete(item_selecionado)
                else:
                    messagebox.showerror("Erro", "Não foi possível excluir o cliente. Verifique se existem contas vinculadas a ele.")
            else:
                messagebox.showerror("Erro", "Cliente não encontrado.")

    def incluir_cliente(self):
        AdicionarClientes(self._janela)

            

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()