import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Depositar:
    def __init__(self, janela_anterior, conta_corrente):
        self.janela_anterior = janela_anterior
        self.conta_corrente = conta_corrente
        self.valor_deposito = None

    def abrir_janela(self):
        self._janela = tk.Toplevel(self.janela_anterior)
        self._janela.title("Depositar")
        self._janela.geometry('300x200')

        self.lbl_valor = tk.Label(self._janela, text='Valor do Depósito: ')
        self.lbl_valor.pack()

        self.etr_valor = tk.Entry(self._janela, width=20)
        self.etr_valor.pack()

        btn_depositar = tk.Button(self._janela, text='Depositar', command=self.depositar)
        btn_depositar.pack(pady=10)

    def depositar(self):
        valor = self.etr_valor.get()
        if valor and valor.isdigit():
            valor = int(valor)
            resultado = self.conta_corrente.set_depositar(valor)
            if resultado:
                messagebox.showinfo("Sucesso", f"Depósito de R${valor} realizado com sucesso!")
                self._janela.destroy()
                self.janela_anterior.deiconify()
            else:
                messagebox.showerror("Erro", "A conta está desativada. O depósito não pode ser realizado.")
        else:
            messagebox.showerror("Erro", "Por favor, insira um valor válido para o depósito.")
