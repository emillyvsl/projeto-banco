import tkinter as tk
from tkinter import messagebox
import sys
sys.path.insert(0, './')
sys.path.insert(0, './classes')
from classes.banco import Banco

class CadastrarBanco:
    def __init__(self, janela_anterior):
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(self.janela_anterior)
        self._janela.title("Cadastrar Banco")
        self._janela.geometry('500x500')
        self.bancos = [] 

        self.lbl_nome = tk.Label(self._janela, text='Nome: ')
        self.lbl_nome.grid(row=0, column=0)
        self.etr = tk.Entry(self._janela)
        self.etr.grid(row=0, column=1)

        btn_cadastrar = tk.Button(self._janela, text='Cadastrar', command=self.cadastrarBanco)
        btn_cadastrar.grid(row=1, column=1)

        btn_voltar = tk.Button(self._janela, text='Voltar', command=self.voltar)
        btn_voltar.grid(row=2, column=1)

        self.banco = None  # Inicializa o atributo como None

    def cadastrarBanco(self):
        nome_banco = self.etr.get()
        self.banco = Banco(nome_banco)  # Instância da classe Banco, passando o valor obtido do widget Entry
        lbl = tk.Label(self._janela, text=f"ID: {self.banco.numero}\nNome: {self.banco.nome}")
        lbl.grid(row=3, column=1)
        messagebox.showinfo("Sucesso", "Banco cadastrado com sucesso!")
        self.bancos.append(self.banco)

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()
