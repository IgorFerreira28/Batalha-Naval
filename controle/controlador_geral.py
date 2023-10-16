from limite.tela_geral import TelaGeral
from controle.controlador_jogador import ControladorJogador
from controle.controlador_partida import ControladorPartida

class ControladorGeral:

    def __init__(self):
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_partida = ControladorPartida(self)
        self.__tela_geral = TelaGeral()

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador
    
    @property
    def controlador_partida(self):
        return self.__controlador_partida
    

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_jogador(self):
        self.__controlador_jogador.abre_tela()
    
    def cadastra_oceano(self):
        self.__controlador_partida.abre_tela_oceano()

    def cadastra_partida(self):
        self.__controlador_partida.abre_tela()
    
    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_jogador, 0: self.encerra_sistema}

        while True:
            try:
                opcao_escolhida = self.__tela_geral.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            except KeyError:
                print("Opção inválida. Por favor, escolha uma opção válida.")
