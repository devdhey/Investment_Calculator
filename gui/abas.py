# calculadora_investimento/gui/abas.py
import tkinter as tk
from tkinter import ttk
from Calculos.investimento import calcular_investimento_necessario, calcular_retorno_investimento

class AbaInvestimentoNecessario:
    def __init__(self, notebook):
        self.frame = tk.Frame(notebook)

        tk.Label(self.frame, text="Nome do ativo:").pack()
        self.entrada_ativo = tk.Entry(self.frame)
        self.entrada_ativo.pack()

        tk.Label(self.frame, text="Preço da cota:").pack()
        self.entrada_preco = tk.Entry(self.frame)
        self.entrada_preco.pack()

        tk.Label(self.frame, text="Dividendo por cota:").pack()
        self.entrada_dividendo = tk.Entry(self.frame)
        self.entrada_dividendo.pack()

        tk.Label(self.frame, text="Retorno desejado:").pack()
        self.entrada_retorno = tk.Entry(self.frame)
        self.entrada_retorno.pack()

        frame_button = tk.Frame(self.frame)
        frame_button.pack(pady=10)

        tk.Button(frame_button, text="Calcular", command=self.calcular).pack(side="left", padx=10)
        tk.Button(frame_button, text="Limpar", command=self.limpar_campos).pack(side="left", padx=10)

        self.resultado_label = tk.Label(self.frame, text="")
        self.resultado_label.pack()

    def calcular(self):
        try:
            preco = float(self.entrada_preco.get())
            dividendo = float(self.entrada_dividendo.get())
            retorno_desejado = float(self.entrada_retorno.get())
            investimento_necessario = calcular_investimento_necessario(preco, dividendo, retorno_desejado)
            self.resultado_label.config(text=f"Investimento Necessário: R$ {investimento_necessario:.2f}")
        except ValueError:
            self.resultado_label.config(text="Por favor, insira valores numéricos válidos.")

    def limpar_campos(self):
        self.entrada_ativo.delete(0, tk.END)
        self.entrada_preco.delete(0, tk.END)
        self.entrada_dividendo.delete(0, tk.END)
        self.entrada_retorno.delete(0, tk.END)
        self.resultado_label.config(text="")

class AbaRetornoInvestimento:
    def __init__(self, notebook):
        self.frame = tk.Frame(notebook)

        tk.Label(self.frame, text="Nome do ativo:").pack()
        self.entrada_ativo = tk.Entry(self.frame)
        self.entrada_ativo.pack()

        tk.Label(self.frame, text="Preço da cota:").pack()
        self.entrada_preco = tk.Entry(self.frame)
        self.entrada_preco.pack()

        tk.Label(self.frame, text="Dividendo por cota:").pack()
        self.entrada_dividendo = tk.Entry(self.frame)
        self.entrada_dividendo.pack()

        tk.Label(self.frame, text="Valor investido:").pack()
        self.entrada_investimento = tk.Entry(self.frame)
        self.entrada_investimento.pack()

        frame_button = tk.Frame(self.frame)
        frame_button.pack(pady=10)

        tk.Button(frame_button, text="Calcular", command=self.calcular).pack(side="left", padx=10)
        tk.Button(frame_button, text="Limpar", command=self.limpar_campos).pack(side="left", padx=10)

        self.resultado_label = tk.Label(self.frame, text="")
        self.resultado_label.pack()

    def calcular(self):
        try:
            preco = float(self.entrada_preco.get())
            dividendo = float(self.entrada_dividendo.get())
            investimento = float(self.entrada_investimento.get())
            retorno = calcular_retorno_investimento(preco, dividendo, investimento)
            self.resultado_label.config(text=f"Retorno Anual Estimado: R$ {retorno:.2f}")
        except ValueError:
            self.resultado_label.config(text="Por favor, insira valores numéricos válidos.")

    def limpar_campos(self):
        self.entrada_ativo.delete(0, tk.END)
        self.entrada_preco.delete(0, tk.END)
        self.entrada_dividendo.delete(0, tk.END)
        self.entrada_investimento.delete(0, tk.END)
        self.resultado_label.config(text="")