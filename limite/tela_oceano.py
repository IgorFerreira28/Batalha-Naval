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
        layout = [
            [sg.Text('---Posicionando Navios---')],
            [sg.Text('Selecione a coordenada do eixo Y', size=(25, 1)), sg.InputText(key='y')],
            [sg.Text('Selecione a coordenada do eixo X:', size=(25, 1)), sg.InputText(key='x')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window('Posicionamento De Embarcacoes', layout)

        while True:
            event, values = window.Read()

            if event in (None, 'Cancel'):
                break

            try:
                cordenada_y = int(values['y'])
                cordenada_x = int(values['x'])

                if cordenada_y is None:
                    raise ValueError("A coordenada Y não pode ser vazia.")
                if cordenada_x is None:
                    raise ValueError("A coordenada X não pode ser vazia.")
                sg.popup(f"Coordenadas selecionadas: Y={cordenada_y}, X={cordenada_x}")
                window.close()
                return cordenada_y, cordenada_x
                

            except ValueError as ve:
                sg.popup_error(f"Erro: {ve}")

        window.close()
        #layout = [
        #[sg.Text('---Posicionando Navios---')],
        #[sg.Text('Selecione a coordenada do eixo Y', size=(15, 1)), sg.InputText()],
        #[sg.Text('Selecione a coordenada do eixo X:', size=(15, 1)), sg.InputText()],
        #[sg.Submit(), sg.Cancel()]
        #]
        #window = sg.Window('Posicionamento De Embarcacoes').Layout(layout)
        #button, values = window.Read()
        #while True:
        #    try:
        #        cordenada_y = input("Selecione a coordenada do eixo Y: ")
        #        cordenada_x = input("Selecione a coordenada do eixo X: ")

#                if not cordenada_y:
 #                   raise ValueError("A coordenada Y não pode ser vazia.")
  #              if not cordenada_x:
   #                 raise ValueError("A coordenada X não pode ser vazia.")
                
    #            return int(cordenada_y), int(cordenada_x)
     #       except ValueError as ve:
      #          print(f"Erro: {ve}.")
    
    def posiciona_navios_x(self):
        layout = [
            [sg.Text('---Posicionando Navios---')],
            [sg.Text('Informe as coordenadas do eixo X (separadas por espaço):', size=(40, 1)), sg.InputText(key='coordenadas')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window('Posicionamento De Embarcacoes', layout)

        while True:
            event, values = window.Read()

            if event in (None, 'Cancel'):
                break

            try:
                cordenada_x = list(map(int, values['coordenadas'].split()))
                
                if not cordenada_x:
                    raise ValueError("A coordenada X está vazia.")

                sg.popup(f"Coordenadas X informadas: {cordenada_x}")
                window.close()
                return cordenada_x

            except ValueError as ve:
                sg.popup_error(f"ERRO: {ve}")

        window.close()
        #print("---Posicionando Navios---")
        #while True:
        #    try:
        #        cordenada_x = list(map(int, input("Informe as coordenadas do eixo X (separadas por espaço): ").split()))
        #        if not cordenada_x:
        #            raise ValueError("A coordenada X está vazia.")
        #        return cordenada_x
        #    except ValueError as ve:
        #        print(f"ERRO: {ve}")
    
    def posiciona_navios_y(self):
        layout = [
            [sg.Text('---Posicionando Navios---')],
            [sg.Text('Informe as coordenadas do eixo Y (separadas por espaço):', size=(40, 1)), sg.InputText(key='coordenadas')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window('Posicionamento De Embarcacoes', layout)

        while True:
            event, values = window.Read()

            if event in (None, 'Cancel'):
                break

            try:
                cordenada_y = list(map(int, values['coordenadas'].split()))
                
                if not cordenada_y:
                    raise ValueError("A coordenada Y está vazia.")

                sg.popup(f"Coordenadas Y informadas: {cordenada_y}")
                window.close()
                return cordenada_y

            except ValueError as ve:
                sg.popup_error(f"ERRO: {ve}")

        window.close()

        #print("---Posicionando Navios---")
        #while True:
        #    try:
        #        cordenada_y = list(map(int, input("Informe as coordenadas do eixo Y (separadas por espaço): ").split()))
        #        if not cordenada_y:
        #            raise ValueError("A coordenada X está vazia.")
        #       return cordenada_y
        #    except ValueError as ve:
        #        print(f"ERRO: {ve}")
    
    def jogada(self):
        layout = [
            [sg.Text('---Realizando Jogada---')],
            [sg.Text('Selecione a coordenada do eixo Y:', size=(30, 1)), sg.InputText(key='eixo_y')],
            [sg.Text('Selecione a coordenada do eixo X:', size=(30, 1)), sg.InputText(key='eixo_x')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window('Jogada', layout)

        while True:
            event, values = window.Read()

            if event in (None, 'Cancel'):
                break

            try:
                eixo_y = int(values['eixo_y'])
                eixo_x = int(values['eixo_x'])

                if eixo_y is None or eixo_x is None:
                    raise ValueError("As coordenadas não podem ser vazias.")
                
                sg.popup(f"Coordenadas do tiro: Y={eixo_y}, X={eixo_x}")
                window.close()
                return eixo_y, eixo_x

            except ValueError as ve:
                sg.popup_error(f"Erro: {ve}")

        window.close()
        #try:
        #    eixo_y = input("Selecione a cordenada Y do tiro: ")
        #    eixo_x = input("selecione a cordenada X do tiro: ")

        #    if not eixo_y:
        #        raise ValueError("A coordenada Y não pode ser vazia.")
        #    if not eixo_x:
        #        raise ValueError("A coordenada X não pode ser vazia.")
                
        #    return int(eixo_y), int(eixo_x)
        #except ValueError as ve:
        #    print(f"Erro: {ve}.")

    def mostra_mensagem(self, msg):
        print(msg)
    
    def mostrar_oceano(self, tamanho, oceano):
        layout = [
            [sg.Text('---Mostrando Oceano---')]
        ]

        for linha in range(tamanho):
            linha_layout = []
            for coluna in range(tamanho):
                linha_layout.append(sg.Text(f'[{oceano[linha][coluna]}]', size=(5, 1), key=f'pos_{linha}_{coluna}'))
            layout.append(linha_layout)

        window = sg.Window('Oceano', layout)

        while True:
            event, values = window.Read()

            if event in (None, 'Cancel'):
                break

        window.close()
        #for linha in range(tamanho):
        #    if linha == 0:
        #        print(f'Y/X   {linha}', end='   ')
        #    else:
        #        print(f'{linha}', end='   ')
        #print()
        #for linha in range(tamanho):
        #    for coluna in range(tamanho):
        #        if coluna == 0:
        #            print(f' {linha}   [{oceano[linha][coluna]}]', end=' ')
        #       else:
        #            print(f'[{oceano[linha][coluna]}]', end=' ')
        #    print()
