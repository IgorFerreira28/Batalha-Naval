from entidade.oceano import Oceano
from entidade.embarcacao.bote import Bote
from entidade.embarcacao.fragata import Fragata
from entidade.embarcacao.porta_avioes import PortaAvioes
from entidade.embarcacao.submarino import Submarino
from entidade.jogador import Jogador

class Partida:
    def __init__(self, jogador):
        self.__bote1_player = Bote(1)
        self.__bote2_player = Bote(1)
        self.__bote3_player = Bote(1)
        self.__fragata1_player = Fragata(3)
        self.__fragata2_player = Fragata(3)
        self.__porta_avioes_player = PortaAvioes(4)
        self.__submarino1_player = Submarino(2)
        self.__submarino2_player = Submarino(2)

        self.__bote1_computador = Bote(1)
        self.__bote2_computador = Bote(1)
        self.__bote3_computador = Bote(1)
        self.__fragata1_computador = Fragata(3)
        self.__fragata2_computador = Fragata(3)
        self.__porta_avioes_computador = PortaAvioes(4)
        self.__submarino1_computador = Submarino(2)
        self.__submarino2_computador = Submarino(2)

        self.__navios_player = [self.__bote1_player, self.__bote2_player,
                                self.__bote3_player, self.__fragata1_player,
                                self.__fragata2_player, self.__porta_avioes_player,
                                self.__submarino1_player, self.__submarino2_player]
        
        self.__navios_computador = [self.__bote1_computador, self.__bote2_computador,
                                    self.__bote3_computador, self.__fragata1_computador,
                                    self.__fragata2_computador, self.__porta_avioes_computador,
                                    self.__submarino1_computador, self.__submarino2_computador] 
        
        self.__jogador = jogador

    @property
    def jogador(self):
        return self.__jogador
    
    @jogador.setter
    def jogador(self, jogador):
        if isinstance(jogador, Jogador):
            self.__jogador = jogador

    @property
    def navios_player(self):
        return self.__navios_player
    
    @navios_player.setter
    def navios_player(self, navios):
        if isinstance(navios, list):
            self.__navios_player = navios
    
    @property
    def navios_computador(self):
        return self.__navios_computador
    
    @navios_computador.setter
    def navios_computador(self, navios):
        if isinstance(navios, list):
            self.__navios_computador = navios
    
    
    @property
    def oceano_computador(self):
        return self.__monta_oceano.oceano_computador()
    
    @property
    def posicoes_navios_player(self):
        return self.__monta_oceano.posicoes_navios_player()
    
    @property
    def posicoes_navios_computador(self):
        return self.__monta_oceano.posicoes_navios_computador()
    
    @property
    def tamanho(self):
        return self.__monta_oceano.tamanho_oceano()