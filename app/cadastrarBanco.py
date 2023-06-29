import tkinter as tk
import sys

sys.path.append('../')
from classes.banco import Banco


class CadastrarBanco:
    def mostrar(self):
        BB=Banco(self.etr.get())
        lbl = tk.Label(self._janela, text=BB.numero)
        lbl.pack()

    def __init__(self, master):
        self._janela = tk.Toplevel(master)
        self._janela.title("Cadastro de Banco")
        self._janela.geometry('500x500')

        self.etr = tk.Entry(self._janela)
        self.etr.pack()

        bt = tk.Button(self._janela, text='cadastrar', command=self.mostrar)
        bt.pack()

        btn = tk.Button(self._janela, text='Voltar', command=self.voltar)
        btn.pack()

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()
