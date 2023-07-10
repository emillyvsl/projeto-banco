import tkinter as tk

class ContaCorrenteI:
    def __init__(self, janela_anterior):
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(janela_anterior)
        self._janela.title("Conta Corrente")
        self._janela.geometry('500x500')


        btn_depositar = tk.Button(self._janela, text='Depositar')
        btn_depositar.grid(row=6, column=1)
       
        btn_sacar = tk.Button(self._janela, text='Sacar')
        btn_sacar.grid(row=6, column=2)

        btn_listar = tk.Button(self._janela, text='Listar Contas')
        btn_listar.grid(row=6, column=3)
       
        btn_incluir = tk.Button(self._janela, text='Incluir')
        btn_incluir.grid(row=6, column=4)

        btn_excluir = tk.Button(self._janela, text='Excluir')
        btn_excluir.grid(row=6, column=5)

        btn = tk.Button(self._janela, text='Voltar', command=self.voltar)
        btn.grid(row=6, column=6)
       
    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()