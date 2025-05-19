# README - Calculadora de Investimento

Este README fornece uma visão geral da aplicação Calculadora de Investimento, explica o propósito do arquivo `main.py` e descreve como executar a aplicação.

## Visão Geral da Aplicação

A Calculadora de Investimento é uma aplicação desktop desenvolvida em Python utilizando a biblioteca Tkinter para a interface gráfica. Ela oferece duas funcionalidades principais para auxiliar investidores:

1.  **Calcular Investimento Necessário:** Permite ao usuário determinar o montante de investimento inicial necessário para atingir um determinado retorno anual desejado, com base no preço da cota de um ativo e no dividendo por cota.
2.  **Calcular Retorno com Investimento:** Permite ao usuário calcular o retorno anual estimado de um investimento já realizado, com base no preço da cota, no dividendo por cota e no valor total investido.

A aplicação possui uma interface amigável com duas abas distintas para cada uma dessas funcionalidades, facilitando a entrada de dados e a visualização dos resultados.

## Arquivo `main.py`

O arquivo `main.py` é o ponto de entrada principal da aplicação. Sua principal responsabilidade é inicializar e iniciar a interface gráfica do usuário. As principais ações realizadas por `main.py` são:

* **Importação de Módulos:** Importa os módulos necessários para executar a aplicação, principalmente:
    * `tkinter as tk`: A biblioteca Tkinter para a criação da interface gráfica básica.
    * `from gui.janela_principal import JanelaPrincipal`: Importa a classe `JanelaPrincipal` do arquivo `janela_principal.py` localizado na pasta `gui/`. Esta classe é responsável pela criação da janela principal da aplicação e pela organização das abas.

* **Criação da Janela Principal:** Cria uma instância da janela raiz do Tkinter (`root = tk.Tk()`). Esta janela serve como o contêiner principal para todos os elementos da interface gráfica.

* **Instanciação da Aplicação:** Cria uma instância da classe `JanelaPrincipal` (`app = JanelaPrincipal(root)`), passando a janela raiz como argumento. Isso inicializa a interface da calculadora, incluindo a criação do notebook de abas e o conteúdo de cada aba.

* **Loop Principal da Aplicação:** Inicia o loop principal da aplicação Tkinter (`root.mainloop()`). Este loop é essencial para que a interface gráfica seja exibida, responda às interações do usuário (como cliques em botões e entrada de texto) e continue em execução até que a janela seja fechada.

**Em resumo, `main.py` é o arquivo que dá o pontapé inicial na execução da aplicação, criando a janela principal e gerenciando o ciclo de vida da interface gráfica.**

## Estrutura do Projeto

A aplicação está organizada em diferentes pastas para separar as responsabilidades do código:

* **`gui/`:** Contém todos os arquivos relacionados à interface gráfica do usuário, incluindo a definição da janela principal (`janela_principal.py`) e o conteúdo de cada aba (`abas.py`).
* **`calculos/`:** Contém os arquivos com a lógica de cálculo financeira da aplicação (`investimento.py`).
* **`main.py`:** O arquivo principal que inicia a aplicação, criando a janela principal e orquestrando a interface.

## Como Executar a Aplicação

Para executar a Calculadora de Investimento, siga os seguintes passos:

1.  **Certifique-se de ter o Python instalado em seu sistema.** A aplicação foi desenvolvida em Python e requer um interpretador Python para ser executada. Recomenda-se usar uma versão recente do Python 3.
2.  **Navegue até o diretório raiz do projeto** no seu terminal ou prompt de comando. Este é o diretório que contém o arquivo `main.py` e as pastas `gui/` e `calculos/`.
3.  **Execute o seguinte comando:**

    ```bash
    python main.py
    ```

    ou, dependendo da sua configuração:

    ```bash
    python3 main.py
    ```

4.  Após executar o comando, a janela da Calculadora de Investimento deverá abrir, permitindo que você utilize as funcionalidades de cálculo de investimento.

## Próximos Passos e Contribuições

Este projeto serve como uma ferramenta básica para cálculos de investimento. Futuras melhorias podem incluir:

* Implementação de mais tipos de cálculos de investimento.
* Opções para salvar e carregar cálculos.
* Melhorias na interface do usuário e na apresentação dos resultados.
* Validação de entrada de dados mais robusta.

Contribuições são bem-vindas! Se você tiver ideias para melhorias ou encontrar algum problema, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Esperamos que esta aplicação seja útil para suas análises de investimento!
