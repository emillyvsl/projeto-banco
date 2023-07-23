import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
sys.path.insert(0, './')
sys.path.insert(0, './classes')

from classes.cliente import Cliente

class EditarCliente:
    def __init__(self, cliente):
        self._cliente = cliente
        self._janela = tk.Toplevel()
        self._janela.title("Editar Cliente")
        self._janela.geometry('400x300')

        lbl_nome = tk.Label(self._janela, text="Nome:")
        lbl_nome.pack()
        self.entry_nome = tk.Entry(self._janela)
        self.entry_nome.insert(tk.END, cliente.nome)
        self.entry_nome.pack()

        lbl_cpf = tk.Label(self._janela, text="CPF:")
        lbl_cpf.pack()
        self.entry_cpf = tk.Entry(self._janela)
        self.entry_cpf.insert(tk.END, cliente.cpf)
        self.entry_cpf.pack()

        lbl_endereco = tk.Label(self._janela, text="Endereço:")
        lbl_endereco.pack()
        self.entry_endereco = tk.Entry(self._janela)
        self.entry_endereco.insert(tk.END, cliente.endereco)
        self.entry_endereco.pack()

        btn_salvar = tk.Button(self._janela, text="Salvar", command=self.salvar_cliente)
        btn_salvar.pack()

    def salvar_cliente(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        endereco = self.entry_endereco.get()

        self._cliente.nome = nome
        self._cliente.cpf = cpf  # Corrigido aqui - atribuir ao cpf do cliente
        self._cliente.endereco = endereco  # Corrigido aqui - atribuir ao endereço do cliente

        messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
        self._janela.destroy()
