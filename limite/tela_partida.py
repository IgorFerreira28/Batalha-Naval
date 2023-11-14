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
        print("-------- Início Partida --------")
        id = int(input("Digite o ID do jogador que jogará está partida: "))
        tamanho_oceano = int(input("Tamanho do oceano: "))

        return {"id": id, "tamanho_oceano": tamanho_oceano}
    
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