**anotações sobre janela_principal.py e abas.py**

gui/janela_principal.py: 
    Contém a classe JanelaPrincipal, responsável por criar a janela principal e o ttk.Notebook para as abas. Ele também instancia as classes que representam cada aba.

gui/abas.py: Define as classes AbaInvestimentoNecessario e AbaRetornoInvestimento.
    Cada classe representa uma aba da sua calculadora, contendo os widgets (labels, entradas, botões) e os métodos para lidar com os eventos (como o clique nos botões Calcular e Limpar). 
    Note que agora as funções de cálculo e limpeza estão dentro dessas classes, referenciando os widgets específicos de cada aba usando self.
