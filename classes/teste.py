
from banco import Banco
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca
bb = Banco('bb')


c = ContaCorrente('maria',100,bb)
c.set_depositar(100)
c.set_sacar(10)
c.saldo
c.set_depositar(500)
print(c.extrato())

cp = ContaPoupanca('joao',bb,100)
cp.set_depositar(500)
print(cp.saldo)
cp.set_sacar(400)
# print(cp.encerrarConta())
print(cp.extrato())
import tkinter as tk
from tkinter import filedialog

# Cria a janela principal
janela = tk.Tk()
def salvar_lista():
    # Obtém o caminho do arquivo usando o seletor de arquivo do Tkinter
    arquivo = filedialog.asksaveasfile(defaultextension=".txt")
    
    # Verifica se o usuário selecionou um arquivo
    if arquivo is None:
        return
    
    # Obtém a lista de informações
    lista_informacoes = c.extrato()  # Sua lista de informações aqui
    
    # Escreve as informações no arquivo
    for item in lista_informacoes:
        arquivo.write(item + "\n")
    
    # Fecha o arquivo
    arquivo.close()

# Cria um botão para salvar a lista
botao_salvar = tk.Button(janela, text="Salvar Lista", command=salvar_lista)
botao_salvar.pack()

# Inicia o loop principal do Tkinter
janela.mainloop()
