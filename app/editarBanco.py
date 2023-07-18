import tkinter as tk
from tkinter import messagebox
import sys
sys.path.insert(0, './')
sys.path.insert(0, './classes')

from classes.banco import Banco


class EditarBanco:
    def __init__(self, banco):
        self._banco = banco
        self._janela = tk.Toplevel()
        self._janela.title("Editar Banco")
        self._janela.geometry('400x300')

        lbl_nome = tk.Label(self._janela, text="Nome:")
        lbl_nome.pack()
        self.entry_nome = tk.Entry(self._janela)
        self.entry_nome.insert(tk.END, banco.nome)
        self.entry_nome.pack()

        btn_salvar = tk.Button(self._janela, text="Salvar", command=self.salvar_banco)
        btn_salvar.pack()

    def salvar_banco(self):
        nome = self.entry_nome.get()

        self._banco.nome = nome

        messagebox.showinfo("Sucesso", "Banco atualizado com sucesso!")
        self._janela.destroy()
