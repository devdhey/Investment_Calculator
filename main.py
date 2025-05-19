# calculadora_investimento/main.py
import tkinter as tk
from gui.janela_principal import JanelaPrincipal

if __name__ == "__main__":
    root = tk.Tk()
    app = JanelaPrincipal(root)
    root.mainloop()
