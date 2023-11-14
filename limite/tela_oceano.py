import PySimpleGUI as sg


class TelaOceano:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.__window.Read()
        if values['1']:
            opcao = 1
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    
    def close(self):
        self.__window.Close()
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- TELA OCEANO ---------', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Realizar Jogada',"RD1", key='1')],
            [sg.Radio('Mostrar Jogadas',"RD1", key='2')],
            [sg.Radio('Mostrar Meu Oceano',"RD1", key='3')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Jogo de Batalha Naval').Layout(layout)

    def posiciona_navios(self):
        print("---Posicionando Navios---")
        while True:
            try:
                cordenada_y = input("Selecione a coordenada do eixo Y: ")
                cordenada_x = input("Selecione a coordenada do eixo X: ")

                if not cordenada_y:
                    raise ValueError("A coordenada Y não pode ser vazia.")
                if not cordenada_x:
                    raise ValueError("A coordenada X não pode ser vazia.")
                
                return int(cordenada_y), int(cordenada_x)
            except ValueError as ve:
                print(f"Erro: {ve}.")
    
    def posiciona_navios_x(self):
        print("---Posicionando Navios---")
        while True:
            try:
                cordenada_x = list(map(int, input("Informe as coordenadas do eixo X (separadas por espaço): ").split()))
                if not cordenada_x:
                    raise ValueError("A coordenada X está vazia.")
                return cordenada_x
            except ValueError as ve:
                print(f"ERRO: {ve}")
    
    def posiciona_navios_y(self):
        print("---Posicionando Navios---")
        while True:
            try:
                cordenada_y = list(map(int, input("Informe as coordenadas do eixo Y (separadas por espaço): ").split()))
                if not cordenada_y:
                    raise ValueError("A coordenada X está vazia.")
                return cordenada_y
            except ValueError as ve:
                print(f"ERRO: {ve}")
    
    def jogada(self):
        try:
            eixo_y = input("Selecione a cordenada Y do tiro: ")
            eixo_x = input("selecione a cordenada X do tiro: ")

            if not eixo_y:
                raise ValueError("A coordenada Y não pode ser vazia.")
            if not eixo_x:
                raise ValueError("A coordenada X não pode ser vazia.")
                
            return int(eixo_y), int(eixo_x)
        except ValueError as ve:
            print(f"Erro: {ve}.")

    def mostra_mensagem(self, msg):
        print(msg)
    
    def mostrar_oceano(self, tamanho, oceano):
        for linha in range(tamanho):
            if linha == 0:
                print(f'Y/X   {linha}', end='   ')
            else:
                print(f'{linha}', end='   ')
        print()
        for linha in range(tamanho):
            for coluna in range(tamanho):
                if coluna == 0:
                    print(f' {linha}   [{oceano[linha][coluna]}]', end=' ')
                else:
                    print(f'[{oceano[linha][coluna]}]', end=' ')
            print()
