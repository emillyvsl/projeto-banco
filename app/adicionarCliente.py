import tkinter as tk
import sys
sys.path.insert(0, './')
sys.path.insert(0, './classes')
from classes.cliente import Cliente

class AdicionarClientes:

    def adicionarCliente(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        endereco = self.ent_endereco.get()
        cli = Cliente(nome, cpf, endereco)

        lbl_info = tk.Label(self._janela, text=f"ID: {cli.numero}\nNome: {cli.nome}\nCPF: {cli.cpf}\nEndereço: {cli.endereco}")
        lbl_info.grid(row=4, columnspan=2)


    def __init__(self, janela_anterior):
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(janela_anterior)
        self._janela.title("Adicionar clientes")
        self._janela.geometry('500x500')

        self.lbl_nome = tk.Label(self._janela, text = 'Nome: ')
        self.lbl_nome.grid(row=0, column=0)
        self.ent_nome = tk.Entry(self._janela )
        self.ent_nome.grid(row=0, column=1)

        self.lbl_cpf = tk.Label(self._janela, text = 'CPF: ')
        self.lbl_cpf.grid(row=1, column=0)
        self.ent_cpf = tk.Entry(self._janela )
        self.ent_cpf.grid(row=1, column=1)

        self.lbl_endereco = tk.Label(self._janela, text = 'Endereço: ')
        self.lbl_endereco.grid(row=2, column=0)
        self.ent_endereco = tk.Entry(self._janela )
        self.ent_endereco.grid(row=2, column=1)

        btn_salvar = tk.Button(self._janela, text='Salvar', command=self.adicionarCliente)
        btn_salvar.grid(row=3, columnspan=2)

    
        btn = tk.Button(self._janela, text='Voltar', command=self.voltar)
        btn.grid(row=4, columnspan=2)
       
    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()