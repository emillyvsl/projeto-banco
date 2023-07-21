import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Sacar:
    def __init__(self, janela_anterior, conta_corrente):
        self.janela_anterior = janela_anterior
        self.conta_corrente = conta_corrente
        self.valor_saque = None

    def abrir_janela(self):
        self._janela = tk.Toplevel(self.janela_anterior)
        self._janela.title("Sacar")
        self._janela.geometry('300x200')

        self.lbl_valor = tk.Label(self._janela, text='Valor do Saque: ')
        self.lbl_valor.pack()

        self.etr_valor = tk.Entry(self._janela, width=20)
        self.etr_valor.pack()

        btn_sacar = tk.Button(self._janela, text='Sacar', command=self.sacar)
        btn_sacar.pack(pady=10)

    def sacar(self):
        valor = self.etr_valor.get()
        if valor and valor.isdigit():
            valor = int(valor)
            resultado = self.conta_corrente.set_sacar(valor)
            if resultado == "sem saldo":
                messagebox.showerror("Erro", "Saldo insuficiente para o saque.")
            elif resultado:
                messagebox.showinfo("Sucesso", f"Saque de R${valor} realizado com sucesso!")
                self._janela.destroy()
                self.janela_anterior.deiconify()
            else:
                messagebox.showerror("Erro", "A conta está desativada ou sem saldo. O saque não pode ser realizado.")
        else:
            messagebox.showerror("Erro", "Por favor, insira um valor válido para o saque.")
