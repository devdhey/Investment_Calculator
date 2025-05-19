# Estrutura da Pasta `calculos/` - Projeto Calculadora de Investimento

Esta seção descreve o conteúdo e o funcionamento da pasta `calculos/` dentro do projeto da Calculadora de Investimento. O principal objetivo desta pasta é encapsular toda a lógica de cálculo financeira da aplicação, separando-a da interface gráfica do usuário (localizada na pasta `gui/`).

## Conteúdo da Pasta `calculos/`

A pasta `calculos/` contém os seguintes arquivos:

* **`__init__.py`:** Este arquivo, mesmo que esteja vazio, indica que a pasta `calculos` é um pacote Python. Isso permite que outros módulos do projeto importem os arquivos dentro desta pasta como módulos (por exemplo, `from calculos.investimento import calcular_investimento_necessario`).

* **`investimento.py`:** Este arquivo contém as funções que implementam a lógica de cálculo específica para investimentos. Atualmente, ele inclui as seguintes funções:

    * **`calcular_investimento_necessario(preco_cota, dividendo_por_cota, retorno_desejado_percentual)`:**
        * **Propósito:** Calcula o montante de investimento necessário para atingir um determinado retorno anual desejado, com base no preço atual da cota de um ativo e no dividendo pago por cota.
        * **Parâmetros de Entrada:**
            * `preco_cota`: O preço atual de uma única cota do ativo (tipo float ou int).
            * `dividendo_por_cota`: O valor do dividendo pago por cada cota do ativo em um período (geralmente anual) (tipo float ou int).
            * `retorno_desejado_percentual`: A porcentagem de retorno anual desejada sobre o investimento (tipo float ou int).
        * **Retorno:** Retorna o valor do investimento necessário (tipo float). Retorna `float('inf')` se o dividendo por cota for zero, evitando divisão por zero.
        * **Validação:** Realiza uma validação básica para garantir que os valores de entrada (preço da cota e retorno desejado) não sejam negativos e que o dividendo por cota não seja negativo. Lança um `ValueError` se os valores forem inválidos.

    * **`calcular_retorno_investimento(preco_cota, dividendo_por_cota, valor_investido)`:**
        * **Propósito:** Calcula o retorno anual estimado de um investimento, dado o preço da cota, o dividendo por cota e o valor total investido.
        * **Parâmetros de Entrada:**
            * `preco_cota`: O preço atual de uma única cota do ativo (tipo float ou int).
            * `dividendo_por_cota`: O valor do dividendo pago por cada cota do ativo em um período (geralmente anual) (tipo float ou int).
            * `valor_investido`: O montante total investido no ativo (tipo float ou int).
        * **Retorno:** Retorna o valor do retorno anual estimado (tipo float).
        * **Validação:** Realiza uma validação básica para garantir que os valores de entrada (preço da cota e valor investido) não sejam negativos e que o dividendo por cota não seja negativo. Lança um `ValueError` se os valores forem inválidos.

## Responsabilidades da Pasta `calculos/`

A pasta `calculos/` tem como responsabilidade principal:

* **Implementar a lógica de negócio:** Contém as funções que realizam os cálculos financeiros específicos da aplicação.
* **Isolar a lógica da interface:** Não possui conhecimento sobre como os dados são obtidos ou como os resultados são exibidos ao usuário. Sua única preocupação é realizar os cálculos corretamente com os dados fornecidos.
* **Promover a reusabilidade:** As funções dentro desta pasta podem ser chamadas por diferentes partes da aplicação (ou até mesmo por outras aplicações, se necessário), sem depender da interface gráfica específica.
* **Facilitar testes:** A lógica de cálculo isolada pode ser testada unitariamente de forma mais fácil e eficiente, garantindo a correção dos resultados.

Ao separar a lógica de cálculo na pasta `calculos/`, o projeto se torna mais organizado, manutenível e escalável. Alterações na interface gráfica (`gui/`) não exigem modificações na lógica de cálculo, e vice-versa, a menos que os requisitos de cálculo mudem. Isso também facilita a colaboração entre desenvolvedores focados na interface e aqueles focados na lógica de negócio.
