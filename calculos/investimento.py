# calculadora_investimento/calculos/investimento.py

def calcular_investimento_necessario(preco_cota, dividendo_por_cota, retorno_desejado_percentual):
    """Calcula o investimento necessário para atingir o retorno desejado."""
    if preco_cota <= 0 or dividendo_por_cota < 0 or retorno_desejado_percentual < 0:
        raise ValueError("Valores inválidos para o cálculo.")
    retorno_desejado = retorno_desejado_percentual / 100
    investimento_necessario = (retorno_desejado * preco_cota) / (dividendo_por_cota / preco_cota) if dividendo_por_cota > 0 else float('inf')
    return investimento_necessario

def calcular_retorno_investimento(preco_cota, dividendo_por_cota, valor_investido):
    """Calcula o retorno anual estimado com base no investimento."""
    if preco_cota <= 0 or dividendo_por_cota < 0 or valor_investido < 0:
        raise ValueError("Valores inválidos para o cálculo.")
    numero_de_cotas = valor_investido / preco_cota
    retorno_anual = numero_de_cotas * dividendo_por_cota
    return retorno_anual