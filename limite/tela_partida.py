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
        self.close()
        return opcao
    
    def comecar_partida(self):
        layout = [
            [sg.Text('-------- Início Partida --------')],
            [sg.Text('Digite o ID do jogador que jogará esta partida:'), sg.InputText(key='id')],
            [sg.Text('Tamanho do oceano:'), sg.InputText(key='tamanho_oceano')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window('Início da Partida', layout)

        while True:
            event, values = window.Read()

            if event in (None, 'Cancel'):
                break

            try:
                jogador_id = int(values['id'])
                tamanho_oceano = int(values['tamanho_oceano'])

                if jogador_id is None or tamanho_oceano is None:
                    raise ValueError("O ID do jogador e o tamanho do oceano não podem ser vazios.")

                sg.popup(f"Informações da Partida: ID do Jogador={jogador_id}, Tamanho do Oceano={tamanho_oceano}")
                window.close()
                return {"id": jogador_id, "tamanho_oceano": tamanho_oceano}

            except ValueError as ve:
                sg.popup_error(f"Erro: {ve}")

        window.close()
    
    def mostra_mensagem(self, msg):
        return msg

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
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