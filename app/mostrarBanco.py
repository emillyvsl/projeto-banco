import tkinter as tk
import sys
sys.path.append('../')
from classes.banco import Banco

class MostrarBanco:

    def mostrarBancos(self):
        lista_bancos = Banco.mostrarBancos()
        for nome_banco in lista_bancos:
            lbl = tk.Label(self._janela, text=nome_banco)
            lbl.pack()
    def __init__(self, master):
        self._janela = tk.Toplevel(master)
        self._janela.title("Lista de Bancos")
        self._janela.geometry('500x500')


        btn_mostrar = tk.Button(self._janela, command=self.mostrarBancos, text='Mostrar todos os bancos')
        btn_mostrar.pack()

        btn = tk.Button(self._janela, text='Voltar', command=self.voltar)
        btn.pack()
       
    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()

        

        self._janela.mainloop()