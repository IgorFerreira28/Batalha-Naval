import PySimpleGUI as sg


class TelaPartida:
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
        elif not values['1'] and not values['0']:
            opcao = None
        self.close()
        return opcao

    def comecar_partida(self, lista_jogadores):
        jogador_selecionado = False
        modo_selecionado = False
        layout = [
            [sg.Text('-------- Início Partida --------')],
            [sg.Text('Escolha o jogador que jogará esta partida:')],
            [sg.Listbox(values=[f'{jogador.nome} - ID: {jogador.id}' for jogador in lista_jogadores], size=(30, 5), key='jogadores')],
            [sg.Text('Escolha o Modo de Jogo:')],
            [sg.Radio('Curto', "TAMANHO_OCEANO", key='curto'), sg.Radio('Longo', "TAMANHO_OCEANO", key='longo')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window('Início da Partida', layout)

        while True:
            event, values = window.Read()

            if event in (None, 'Cancel'):
                window.close()
                return None

            if values['jogadores'] and not jogador_selecionado:
                try:
                    info_jogador_selecionado = values['jogadores'][0].split('- ID: ')
                    jogador_id = int(info_jogador_selecionado[1])
                    jogador_selecionado = True
                except (ValueError, IndexError) as ve:
                    sg.popup_error(f"Erro: {ve}")
            if jogador_selecionado and (values['curto'] or values['longo']):
                modo_selecionado = True
                tamanho_oceano = 5 if values['curto'] else 10
                sg.popup(f"Informações da Partida: Jogador={info_jogador_selecionado[0]}, ID={jogador_id}, Tamanho do Oceano={tamanho_oceano}")
                window.close()
                return {"id": jogador_id, "tamanho_oceano": tamanho_oceano}

    def mostra_mensagem(self, msg):
        sg.popup(msg)

    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightBlue')
        layout = [
            [sg.Text('-------- TELA PARTIDA ---------', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Começar Partida',"RD1", key='1')],
            [sg.Radio('Retornar',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Menu Partida').Layout(layout)
    
    def close(self):
        self.__window.Close()
