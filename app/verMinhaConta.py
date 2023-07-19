import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sys

sys.path.insert(0, './')
sys.path.insert(0, './classes')
from classes.contaCorrente import ContaCorrente
from classes.contaPoupanca import ContaPoupanca

class VerMinhaConta():
    def __init__(self, janela_anterior, id, tipo):
        self._conta = None
        self.janela_anterior = janela_anterior
        self._janela = tk.Toplevel(self.janela_anterior)
        self._janela.title("Lista de Bancos")
        self._janela.geometry('700x500')
        
        if tipo == 'Conta Poupança':
            print('jkndsfjkcdsfjkbdsjbsj')
            for i in ContaPoupanca.mostrarContasP():
                if id == i.numero:
                    self._conta = i
                    break
        elif tipo == 'Conta Corrente':
            for i in ContaCorrente.mostrarContasC():
                if id == i.numero:
                    self._conta = i
                    break
        print(f"teste teste{self._conta.nome}")
        # Carregar e exibir a imagem
        imagem = Image.open(r"C:\Users\Emilly\Desktop\Trabalho tesi\Projeto-Banco\app\banco.png")

        imagem = imagem.resize((200, 200))  # Redimensionar a imagem conforme necessário
        self.minha_imagem = ImageTk.PhotoImage(imagem)

        frame_imagem = ttk.Frame(self._janela)
        frame_imagem.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        label_imagem = ttk.Label(frame_imagem, image=self.minha_imagem)
        label_imagem.pack()

        # Exibir o nome da conta
        label_nome_conta = ttk.Label(self._janela, text=self._conta.nome)
        label_nome_conta.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        # Adicionar saldo e banco vinculado
        label_saldo = ttk.Label(self._janela, text=self._conta.saldo)
        label_saldo.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        label_banco_vinculado = ttk.Label(self._janela, text=self._conta.banco)
        label_banco_vinculado.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        # Adicionar botões de saque, depósito e encerramento de conta
        button_saque = ttk.Button(self._janela, text="Saque", command=self.realizar_saque)
        button_saque.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        button_deposito = ttk.Button(self._janela, text="Depósito", command=self.realizar_deposito)
        button_deposito.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        button_encerrar = ttk.Button(self._janela, text="Encerrar Conta", command=self.encerrar_conta)
        button_encerrar.grid(row=3, column=2, padx=10, pady=10, sticky='w')

        # Botão de voltar
        button_voltar = ttk.Button(self._janela, text="Voltar", command=self.voltar)
        button_voltar.grid(row=4, column=2, padx=10, pady=10, sticky='se')

    def realizar_saque(self):
        # Lógica para realizar saque
        pass

    def realizar_deposito(self):
        # Lógica para realizar depósito
        pass

    def encerrar_conta(self):
        # Lógica para encerrar conta
        pass

    def voltar(self):
        self._janela.destroy()
        self.janela_anterior.deiconify()
