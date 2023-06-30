import tkinter as tk

class CriarContaC:
    def __init__(self, master):
        self._janela = tk.Toplevel(master)
        self._janela.title("Criar Conta Corrente")
        self._janela.geometry('500x500')


        lbl_Cliente = tk.Label(self._janela, text = 'Escolha um cliente: ')
        lbl_Cliente.grid(row=0, column=0) 
        ent_Cliente = tk.Entry(self._janela ) #precisa de outro componente que liste os clientes
        ent_Cliente.grid(row=0, column=1)

        lbl_banco= tk.Label(self._janela, text = 'Escola seu banco: ')
        lbl_banco.grid(row=1, column=0)
        ent_banco = tk.Entry(self._janela )
        ent_banco.grid(row=1, column=1)

        btn = tk.Button(self._janela, text='Voltar', command=self.voltar)
        btn.pack()
       
    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()