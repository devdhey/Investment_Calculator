# Estrutura da Pasta `gui/` - Projeto Calculadora de Investimento

Esta seção detalha a organização e o funcionamento da pasta `gui/` (Interface Gráfica do Usuário) dentro do projeto da Calculadora de Investimento. Esta pasta é responsável por toda a parte visual e interativa da aplicação, utilizando a biblioteca Tkinter para criar a interface com o usuário.

## Conteúdo da Pasta `gui/`

A pasta `gui/` contém os seguintes arquivos:

* **`__init__.py`:** Este arquivo, embora geralmente vazio, marca a pasta `gui` como um pacote Python. Isso permite que outros módulos do projeto importem os arquivos dentro desta pasta como módulos (por exemplo, `from gui.janela_principal import JanelaPrincipal`).

* **`janela_principal.py`:** Este arquivo define a classe principal da interface gráfica, chamada `JanelaPrincipal`. Suas responsabilidades incluem:
    * **Criação da Janela Principal:** Inicializa a janela Tkinter (`tk.Tk()`) que serve como container para toda a aplicação.
    * **Configuração da Janela:** Define o título da janela e suas dimensões iniciais (`janela.title()` e `janela.geometry()`).
    * **Gerenciamento de Abas (Notebook):** Utiliza o widget `ttk.Notebook` para criar uma interface com múltiplas abas, permitindo a organização das diferentes funcionalidades da calculadora (cálculo do investimento necessário e cálculo do retorno com investimento) em páginas separadas.
    * **Instanciação das Abas:** Cria instâncias das classes que definem o conteúdo de cada aba (`AbaInvestimentoNecessario` e `AbaRetornoInvestimento` do arquivo `abas.py`) e as adiciona ao `Notebook` com seus respectivos títulos.

* **`abas.py`:** Este arquivo contém as definições das classes que representam cada uma das abas (páginas) dentro do `ttk.Notebook`. Atualmente, ele inclui:
    * **`AbaInvestimentoNecessario`:**
        * **Criação da Aba:** Define um `tk.Frame` que serve como o container para os widgets desta aba.
        * **Widgets de Entrada:** Cria e posiciona os rótulos (`tk.Label`) e campos de entrada de texto (`tk.Entry`) para que o usuário possa inserir os dados necessários para o cálculo do investimento necessário (nome do ativo, preço da cota, dividendo por cota, retorno desejado).
        * **Botões de Ação:** Cria e posiciona os botões "Calcular" e "Limpar" (`tk.Button`). O botão "Calcular" está associado ao método `calcular` desta classe, que coleta os dados dos campos de entrada, chama a função de cálculo apropriada (localizada na pasta `calculos/`) e exibe o resultado. O botão "Limpar" está associado ao método `limpar_campos`, que limpa o conteúdo de todos os campos de entrada e reseta a área de resultado.
        * **Label de Resultado:** Cria um `tk.Label` para exibir o resultado do cálculo ao usuário.
    * **`AbaRetornoInvestimento`:**
        * **Estrutura Similar:** Possui uma estrutura semelhante à `AbaInvestimentoNecessario`, com `tk.Frame` como container, rótulos e campos de entrada para os dados necessários para calcular o retorno com um investimento (nome do ativo, preço da cota, dividendo por cota, valor investido).
        * **Botões de Ação:** Contém botões "Calcular" (associado ao método `calcular` desta classe, que interage com a lógica de cálculo correspondente) e "Limpar" (associado ao método `limpar_campos`).
        * **Label de Resultado:** Um `tk.Label` para exibir o retorno anual estimado.

## Responsabilidades da Pasta `gui/`

Em resumo, a pasta `gui/` é responsável por:

* **Definir a interface visual** da aplicação usando os widgets do Tkinter.
* **Organizar os elementos da interface** em uma estrutura lógica e intuitiva (utilizando abas com o `ttk.Notebook`).
* **Capturar a entrada de dados** do usuário através dos campos de texto (`tk.Entry`).
* **Apresentar os resultados** dos cálculos ao usuário através de rótulos (`tk.Label`).
* **Lidar com as interações do usuário** através de botões (`tk.Button`), acionando as ações de cálculo e limpeza dos campos.
* **Manter a separação entre a apresentação (interface) e a lógica de negócio** (cálculos), que reside em outra parte do projeto (`calculos/`). As classes dentro de `gui/` interagem com a lógica de cálculo, mas não a implementam diretamente.

A organização do código dentro da pasta `gui/` em arquivos separados (um para a janela principal e outro para as abas) contribui para uma melhor modularização e facilita a manutenção e a expansão da interface no futuro.
