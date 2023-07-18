import tkinter as tk
from tkinter import ttk
from verMinhaConta import VerMinhaConta


class MinhaConta:
    def __init__(self, janela_anterior):
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(janela_anterior)
        self._janela.title("Contas")
        self._janela.geometry('700x500')


        # Configurar redimensionamento responsivo
        self._janela.grid_rowconfigure(0, weight=1)
        self._janela.grid_rowconfigure(1, weight=1)
        self._janela.grid_columnconfigure(0, weight=1)

        #escolher qual conta é
        lbl = tk.Label(self._janela,text='Qual o numero da sua conta?')
        lbl.pack()
        self._etr_id = tk.Entry(self._janela, width=40)
        self._etr_id.pack()
        lbl_tipo_conta = tk.Label(self._janela,text='Selecione o tipo de conta:')
        lbl_tipo_conta.pack()
        tipos = ['Conta Corrente','Conta Poupança']
        self.combobox_cliente = ttk.Combobox(self._janela, values=[i for i in tipos], state='readonly')
        self.combobox_cliente.pack()
        
        btn_mostrarConta = tk.Button(self._janela,text='Ver minha conta',command=self.verConta)
        btn_mostrarConta.pack()

    def verConta(self):
        id = self._etr_id.get() 
        tipo = self.combobox_cliente.get()
        VerMinhaConta(self._janela,id,tipo)
        
    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()