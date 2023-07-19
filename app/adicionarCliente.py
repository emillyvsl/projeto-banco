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
        if self.validar_cpf(self.ent_cpf.get()):
            nome = self.ent_nome.get()
            cpf = self.ent_cpf.get()
            endereco = self.ent_endereco.get()
            cli = Cliente(nome, cpf, endereco)
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            self._janela.destroy()  # Fecha a janela de cadastro
            self.janela_anterior.deiconify()  # Exibe a janela anterior
        else:
            messagebox.showinfo("CPF invalido", "Insira um CPF valido!Seu CPF deves estar no seguinte formato:XXX.XXX.XXX-XX")
        
    def validar_cpf(self, cpf):
        # Remover caracteres especiais e espaços em branco
        cpf = ''.join(filter(str.isdigit, cpf))

        # Verificar se o CPF tem 11 dígitos
        if len(cpf) != 11:
            return False

        # Verificar se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False

        # Verificar dígito verificador
        soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma1 * 10) % 11
        if digito1 == 10:
            digito1 = 0
        if digito1 != int(cpf[9]):
            return False

        soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma2 * 10) % 11
        if digito2 == 10:
            digito2 = 0
        if digito2 != int(cpf[10]):
            return False

        return True

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()

