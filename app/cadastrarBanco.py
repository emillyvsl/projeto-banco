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
        self._janela.geometry('700x500')

        self.lbl_nome = tk.Label(self._janela, text='Nome: ')
        self.lbl_nome.grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.etr = tk.Entry(self._janela, width=40)
        self.etr.grid(row=0, column=1, sticky='w', padx=10, pady=5)

        btn_frame = tk.Frame(self._janela)
        btn_frame.grid(row=1, columnspan=2, padx=10, pady=10)

        btn_cadastrar = tk.Button(btn_frame, text='Cadastrar', command=self.cadastrarBanco)
        btn_cadastrar.pack(side='left', padx=5)

        btn_voltar = tk.Button(btn_frame, text='Voltar', command=self.voltar)
        btn_voltar.pack(side='left', padx=5)

        self.banco = None  # Inicializa o atributo como None

    def cadastrarBanco(self):
        nome_banco = self.etr.get()
        self.banco = Banco(nome_banco)  # Instância da classe Banco, passando o valor obtido do widget Entry
        lbl = tk.Label(self._janela, text=f"ID: {self.banco.numero}\nNome: {self.banco.nome}")
        lbl.grid(row=3, column=1, padx=10, pady=10)
        messagebox.showinfo("Sucesso", "Banco cadastrado com sucesso!")
        self._janela.destroy()  # Fecha a janela de cadastro
        self.janela_anterior.deiconify()  # Exibe a janela anterior

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()
