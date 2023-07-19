import tkinter as tk
from tkinter import ttk
from classes.contaPoupanca import ContaPoupanca
from classes.contaCorrente import ContaCorrente

class VerMinhaConta():
    def __init__(self,janela_anterior,id,tipo):
        self.janela_anterior = janela_anterior
        #self.cadastrar_banco = cadastrar_banco
        self._janela = tk.Toplevel(self.janela_anterior)
        self._janela.title("Minha conta")
        self._janela.geometry('700x500')
        self._contaP = ContaPoupanca.mostrarContasP()
        self._contaC = ContaCorrente.mostrarContasC()

        


    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()

    

        self._janela.mainloop()
