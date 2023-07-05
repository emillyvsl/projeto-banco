import tkinter as tk
import sys
from tkinter import ttk
sys.path.insert(0, './')
sys.path.insert(0, './classes')

from classes.banco import Banco

class MostrarBanco:
    def mostrarBancos(self):
        lista_bancos = Banco.mostrarBancos()
        for banco in lista_bancos:
            self.treeview.insert('', 'end', values=banco)


    def __init__(self, janela_anterior):
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(self.janela_anterior)
        self._janela.title("Lista de Bancos")
        self._janela.geometry('500x500')

        colunas = ('ID', 'Nome')
        self.treeview = ttk.Treeview(self._janela, columns=colunas, height=5, show='headings')
        self.treeview.grid(sticky='nsew')

        # Cabeçalhos
        self.treeview.heading('ID', text='ID')
        self.treeview.heading('Nome', text='Nome')

        # Colunas
        self.treeview.column('ID', minwidth=50, width=50)
        self.treeview.column('Nome', minwidth=200, width=200)
        # Barra de rolagem
        scb = ttk.Scrollbar(self._janela, orient=tk.VERTICAL, command=self.treeview.yview)
        scb.grid(row=0, column=1, sticky='ns')
        self.treeview.config(yscrollcommand=scb.set)

        # Chamar a função para mostrar os bancos na tabela
        self.mostrarBancos()

        btn = tk.Button(self._janela, text='Voltar', command=self.voltar)
        btn.grid(row=5, column=0, columnspan=2)
       
    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()

        

        self._janela.mainloop()