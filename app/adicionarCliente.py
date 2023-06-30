import tkinter as tk

class AdicionarClientes:

    #def adicionarCliente():
     #   cli = Cliente()

    def __init__(self, master):
        self._janela = tk.Toplevel(master)
        self._janela.title("Adicionar clientes")
        self._janela.geometry('500x500')

        lbl_nome = tk.Label(self._janela, text = 'Nome: ')
        lbl_nome.grid(row=0, column=0)
        ent_nome = tk.Entry(self._janela )
        ent_nome.grid(row=0, column=1)

        lbl_cpf = tk.Label(self._janela, text = 'CPF: ')
        lbl_cpf.grid(row=1, column=0)
        ent_cpf = tk.Entry(self._janela )
        ent_cpf.grid(row=1, column=1)

        lbl_endereco = tk.Label(self._janela, text = 'Endereço: ')
        lbl_endereco.grid(row=2, column=0)
        ent_endereco = tk.Entry(self._janela )
        ent_endereco.grid(row=2, column=1)

        btn_salvar = tk.Button(self._janela, text='Salvar')
        btn_salvar.grid(row=3, columnspan=2)


        

        btn = tk.Button(self._janela, text='Voltar', command=self.voltar)
        btn.pack()
       
    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()