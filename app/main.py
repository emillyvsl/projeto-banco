import tkinter as tk

class TelaPrincipal:
    def __init__(self,master):
        self._janela = master



master = tk.Tk()
app = TelaPrincipal(master)
master.mainloop()
