import tkinter as tk
import sys
from tkinter import ttk
from cadastrarBanco import CadastrarBanco
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
        #self.cadastrar_banco = cadastrar_banco
        self._janela = tk.Toplevel(self.janela_anterior)
        self._janela.title("Lista de Bancos")
        self._janela.geometry('500x500')

        colunas = ('ID', 'Nome')

        self.treeview = ttk.Treeview(self._janela, columns=colunas, show='headings')
        self.treeview.grid(row=0, column=0, rowspan=5, padx=10, pady=10, sticky='nsew')

        # Configurar redimensionamento responsivo
        self._janela.grid_rowconfigure(0, weight=1)
        self._janela.grid_columnconfigure(0, weight=1)

        # Cabeçalhos
        self.treeview.heading('ID', text='ID')
        self.treeview.heading('Nome', text='Nome')

        # Colunas
        self.treeview.column('ID', minwidth=50, width=50)
        self.treeview.column('Nome', minwidth=200, width=200)

        # Barra de rolagem
        scb = ttk.Scrollbar(self._janela, orient=tk.VERTICAL, command=self.treeview.yview)
        scb.grid(row=0, column=1, rowspan=5, sticky='ns')
        self.treeview.config(yscrollcommand=scb.set)

        # Chamar a função para mostrar os bancos na tabela
        self.mostrarBancos()

        #BOTÕES
        

        frame_btn = tk.Frame(self._janela)
        frame_btn.grid(row=5,column=0)
        
        btn_editar = tk.Button(frame_btn, text='Editar') #command=self.editar
        btn_editar.grid(row=5, column=0)

        btn_excluir = tk.Button(frame_btn, text='Excluir')#,command=self.excluir
        btn_excluir.grid(row=5,column=1)

        btn_incluir = tk.Button(frame_btn, text='Incluir', command=self.incluir_banco)
        btn_incluir.grid(row=5, column=2)


        btn_pesq = tk.Button(frame_btn, text='Pesquisar')
        btn_pesq.grid(row=5,column=3)

        btn = tk.Button(frame_btn, text='Voltar', command=self.voltar)
        btn.grid(row=5, column=4)
        
    def incluir_banco(self):
        CadastrarBanco(self._janela)

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()

    

        self._janela.mainloop()
