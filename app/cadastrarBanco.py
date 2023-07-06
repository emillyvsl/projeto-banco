import tkinter as tk

import sys
from tkinter import messagebox
#from mostrarBanco import MostrarBanco
sys.path.insert(0, './')
sys.path.insert(0, './classes')
from classes.banco import Banco


class CadastrarBanco:
    def cadastrarBanco(self):
        BB=Banco(self.etr.get()) #instância da classe Banco, passando o valor obtido do widget Entry
        lbl = tk.Label(self._janela, text=f"ID: {BB.numero}\nNome: {BB.nome}") #exibirá o valor do atributo numero/nome do objeto BB
        lbl.grid(row=3, column=1)
        messagebox.showinfo("Sucesso", "Banco cadastrado com sucesso!")


    def __init__(self, janela_anterior):
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(self.janela_anterior)
        self._janela.title("Cadastrar Banco")
        self._janela.geometry('500x500')

        self.lbl_nome = tk.Label(self._janela, text='Nome: ')
        self.lbl_nome.grid(row=0, column=0)
        self.etr = tk.Entry(self._janela)
        self.etr.grid(row=0, column=1)

        btn_cadastrar = tk.Button(self._janela, text='cadastrar', command=self.cadastrarBanco)
        btn_cadastrar.grid(row=1, column=1)

        btn = tk.Button(self._janela, text='Voltar', command=self.voltar)
        btn.grid(row=2, column=1)

        btn_ver = tk.Button(self._janela, text='Ver bancos')#command=self.lista_banco
        btn_ver.grid(row=3, column=1)

    # def lista_banco(self):
        # MostrarBanco(self._janela)

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()
