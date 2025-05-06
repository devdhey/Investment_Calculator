import tkinter as tk
from tkinter import ttk, messagebox

def calcular():
    """Calcula o investimento necessário para alcançar um retorno desejado."""
    try:
        ativo = entrada_ativo.get()
        preco_cota = float(entrada_preco.get())
        dividendo_por_cota = float(entrada_dividendo.get())
        retorno_desejado = float(entrada_retorno.get())

        # Cálculo
        quantidade_cotas = retorno_desejado / dividendo_por_cota
        investimento_total = quantidade_cotas * preco_cota

        # Exibe resultado
        resultado_label.config(text=f"Para receber R$ {retorno_desejado:.2f} em dividendos com {ativo}:\n"
                                    f"Você precisará de aproximadamente {int(quantidade_cotas)} cotas.\n"
                                    f"O investimento total necessário será de R$ {investimento_total:.2f}.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def calcular_retorno():
    """Calcula o retorno esperado baseado no valor investido."""
    try:
        ativo = entrada_ativo2.get()
        preco_cota = float(entrada_preco2.get())
        dividendo_por_cota = float(entrada_dividendo2.get())
        investimento = float(entrada_investimento.get())

        # Cálculo
        quantidade_cotas = investimento / preco_cota
        retorno_esperado = quantidade_cotas * dividendo_por_cota

        # Exibe resultado
        resultado_label2.config(text=f"Investindo R$ {investimento:.2f} em {ativo},\n"
                                     f"Você terá comprado aproximadamente {int(quantidade_cotas)} cotas.\n"
                                     f"O retorno esperado será de R$ {retorno_esperado:.2f}.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def limpar_campos():
    """Limpa todos os campos de entrada e o resultado."""
    entrada_ativo.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)
    entrada_dividendo.delete(0, tk.END)
    entrada_retorno.delete(0, tk.END)
    resultado_label.config(text="")

    # Limpa todos da aba 2
    entrada_ativo2.delete(0, tk.END)
    entrada_preco2.delete(0, tk.END)
    entrada_dividendo2.delete(0, tk.END)
    entrada_investimento.delete(0, tk.END)
    resultado_label2.config(text="")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora de Investimento")
janela.geometry("600x500")

# Criando um Notebook para abas
notebook = ttk.Notebook(janela)
notebook.pack(expand=True, fill="both")

# ---- Aba 1: Calcular Investimento Necessário ----
aba1 = tk.Frame(notebook)
notebook.add(aba1, text="Investimento Necessário")

tk.Label(aba1, text="Nome do ativo:").pack()
entrada_ativo = tk.Entry(aba1)
entrada_ativo.pack()

tk.Label(aba1, text="Preço da cota:").pack()
entrada_preco = tk.Entry(aba1)
entrada_preco.pack()

tk.Label(aba1, text="Dividendo por cota:").pack()
entrada_dividendo = tk.Entry(aba1)
entrada_dividendo.pack()

tk.Label(aba1, text="Retorno desejado:").pack()
entrada_retorno = tk.Entry(aba1)
entrada_retorno.pack()

frame_button1 = tk.Frame(aba1)
frame_button1.pack(pady=10)

tk.Button(frame_button1, text="Calcular", command=calcular).pack(side="left", padx=10)
tk.Button(frame_button1, text="Limpar", command=limpar_campos).pack(side="left", padx=10)

resultado_label = tk.Label(aba1, text="")
resultado_label.pack()

# ---- Aba 2: Calcular Retorno com Investimento ----
aba2 = tk.Frame(notebook)
notebook.add(aba2, text="Retorno com Investimento")

tk.Label(aba2, text="Nome do ativo:").pack()
entrada_ativo2 = tk.Entry(aba2)
entrada_ativo2.pack()

tk.Label(aba2, text="Preço da cota:").pack()
entrada_preco2 = tk.Entry(aba2)
entrada_preco2.pack()

tk.Label(aba2, text="Dividendo por cota:").pack()
entrada_dividendo2 = tk.Entry(aba2)
entrada_dividendo2.pack()

tk.Label(aba2, text="Valor investido:").pack()
entrada_investimento = tk.Entry(aba2)
entrada_investimento.pack()

frame_button2 = tk.Frame(aba2)
frame_button2.pack(pady=10)

tk.Button(frame_button2, text="Calcular", command=calcular_retorno).pack(side="left", padx=10)
tk.Button(frame_button2, text="Limpar", command=limpar_campos).pack(side="left", padx=10)

# BOTÃO PARA FECHAR A APLICAÇÃO
button_fechar = ttk.Button(janela,text="Fechar",command=janela.destroy)
# fecha a janela 
button_fechar.pack(pady=10)

#resultados
resultado_label2 = tk.Label(aba2, text="")
resultado_label2.pack()

# Iniciando a interface gráfica
janela.mainloop()
