import tkinter as tk

class CriarConta:
    def __init__(self, master):
        self._janela = tk.Toplevel(master)
        self._janela.title("Criar Conta")
        self._janela.geometry('500x500')

        btn = tk.Button(self._janela, text='Voltar', command=self.voltar)
        btn.pack()
       
    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()