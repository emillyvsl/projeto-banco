import tkinter as tk
from tkinter import filedialog

class MostrarExtrato:
    def __init__(self, janela_anterior, cliente):
        self._cliente = cliente
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(janela_anterior)
        self._janela.title("Extratos")
        self._janela.geometry('700x500')

        self.conteudo_lista = tk.Text(self._janela)
        self.conteudo_lista.pack()

        self.botao_salvar = tk.Button(self._janela, text="Salvar", command=self.salvar_arquivo)
        self.botao_salvar.pack()

        self.botao_voltar = tk.Button(self._janela, text="Voltar", command=self.voltar)
        self.botao_voltar.pack()

        self.exibir_conteudo_lista()

    def exibir_conteudo_lista(self):
        # Obtém a lista de informações
        lista_informacoes = self._cliente.extrato()

        # Limpa o conteúdo do widget de texto
        self.conteudo_lista.delete("1.0", tk.END)

        # Insere o conteúdo da lista no widget de texto
        for item in lista_informacoes:
            self.conteudo_lista.insert(tk.END, item + "\n")

        # Desabilita a entrada de informações no widget de texto
        self.conteudo_lista.config(state=tk.DISABLED)

    def salvar_arquivo(self):
        arquivo = filedialog.asksaveasfile(defaultextension=".txt")

        if arquivo is None:
            return
        conteudo = self.conteudo_lista.get("1.0", tk.END)
        arquivo.write(conteudo)

        arquivo.close()

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()
