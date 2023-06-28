import tkinter as tk

class TelaPrincipal:
    def __init__(self,master):
        self._janela = master

 
        mnu_barra = tk.Menu(self._janela)
        self._janela.config(menu=mnu_barra)
        mnu_banco = tk.Menu(mnu_barra)
        mnu_barra.add_cascade(label='Banco', menu=mnu_banco)
        mnu_banco.add_command(label='Cadastrar banco')

        mnu_banco.add_command(label='Mostrar bancos')
        mnu_banco.add_command(label='Atualizar informações')

        mnu_cliente = tk.Menu(mnu_barra)
        mnu_barra.add_cascade(label='Cliente', menu=mnu_cliente)
        mnu_cliente.add_command(label='Ver clientes')
        mnu_cliente.add_command(label='Adicionar clientes')

        mnu_conta = tk.Menu(mnu_barra)
        mnu_barra.add_cascade(label='Conta', menu=mnu_conta)
        mnu_conta.add_cascade(label='Criar Conta')
        mnu_conta.add_cascade(label='Conta Corrente')
        mnu_conta.add_cascade(label='Conta Poupança') 
    

master = tk.Tk()
app = TelaPrincipal(master)
master.mainloop()
