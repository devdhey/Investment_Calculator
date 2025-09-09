# calculadora_investimento/gui/janela_principal.py
import tkinter as tk
from tkinter import ttk
from gui.abas import AbaInvestimentoNecessario, AbaRetornoInvestimento

class JanelaPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Investimento")
        master.geometry("600x500")

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill="both")

        self.aba_investimento = AbaInvestimentoNecessario(self.notebook)
        self.notebook.add(self.aba_investimento.frame, text="Investimento Necessário")

        self.aba_retorno = AbaRetornoInvestimento(self.notebook)
        self.notebook.add(self.aba_retorno.frame, text="Retorno Anual com Investimento")