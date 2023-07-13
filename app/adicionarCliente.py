import tkinter as tk
from tkinter import messagebox
import sys
sys.path.insert(0, './')
sys.path.insert(0, './classes')
from classes.cliente import Cliente

class AdicionarClientes:
    def __init__(self, janela_anterior):
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(janela_anterior)
        self._janela.title("Adicionar clientes")
        self._janela.geometry('700x500')

        self.lbl_nome = tk.Label(self._janela, text='Nome:')
        self.lbl_nome.grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.ent_nome = tk.Entry(self._janela, width=40)
        self.ent_nome.grid(row=0, column=1, sticky='w', padx=10, pady=5)

        self.lbl_cpf = tk.Label(self._janela, text='CPF:')
        self.lbl_cpf.grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.ent_cpf = tk.Entry(self._janela, width=40)
        self.ent_cpf.grid(row=1, column=1, sticky='w', padx=10, pady=5)

        self.lbl_endereco = tk.Label(self._janela, text='Endereço:')
        self.lbl_endereco.grid(row=2, column=0, sticky='w', padx=10, pady=5)
        self.ent_endereco = tk.Entry(self._janela, width=40)
        self.ent_endereco.grid(row=2, column=1, sticky='w', padx=10, pady=5)

        btn_frame = tk.Frame(self._janela)
        btn_frame.grid(row=3, columnspan=2, padx=10, pady=10)

        btn_salvar = tk.Button(btn_frame, text='Salvar', command=self.adicionarCliente)
        btn_salvar.pack(side='left', padx=5)

        btn_voltar = tk.Button(btn_frame, text='Voltar', command=self.voltar)
        btn_voltar.pack(side='left', padx=5)

    def adicionarCliente(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        endereco = self.ent_endereco.get()
        cli = Cliente(nome, cpf, endereco)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        lbl_info = tk.Label(self._janela, text=f"ID: {cli.numero}\nNome: {cli.nome}\nCPF: {cli.cpf}\nEndereço: {cli.endereco}")
        lbl_info.grid(row=6, columnspan=2, padx=10, pady=10)

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()
