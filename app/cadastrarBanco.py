import tkinter as tk

import sys
sys.path.append('../')
from classes.banco import Banco


class CadastrarBanco:
    def cadastrarBanco(self):
        BB=Banco(self.etr.get()) #instância da classe Banco, passando o valor obtido do widget Entry

        lbl = tk.Label(self._janela, text=f"ID: {BB.numero}\nNome: {BB.nome}") #exibirá o valor do atributo numero/nome do objeto BB
        lbl.grid(row=3, column=1)

    def __init__(self, master):
        self._janela = tk.Toplevel(master)
        self._janela.title("Cadastro de Banco")
        self._janela.geometry('500x500')

        self.lbl_nome = tk.Label(self._janela, text='Nome: ')
        self.lbl_nome.grid(row=0, column=0)
        self.etr = tk.Entry(self._janela)
        self.etr.grid(row=0, column=1)

        btn_cadastrar = tk.Button(self._janela, text='cadastrar', command=self.cadastrarBanco)
        btn_cadastrar.grid(row=1, column=1)

        btn = tk.Button(self._janela, text='Voltar', command=self.voltar)
        btn.grid(row=2, column=1)

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()
