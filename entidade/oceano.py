class Oceano:
    def __init__(self, tamanho_oceano):
        self.__tamanho_oceano = tamanho_oceano
        self.__posicoes_navios_player = []
        self.__posicoes_navios_computador  = []
        self.__oceano_player = [[0] * self.__tamanho_oceano for j in range(self.__tamanho_oceano)]
        self.__oceano_computador = [[0] * self.__tamanho_oceano for j in range(self.__tamanho_oceano)]

    @property
    def tamanho_oceano(self):
        return self.__tamanho_oceano
    
    @tamanho_oceano.setter
    def tamanho_oceano(self, tamanho):
        if isinstance(tamanho, int):
            self.__tamanho_oceano = tamanho

    @property
    def oceano_player(self):
        return self.__oceano_player
    
    @oceano_player.setter
    def oceano_player(self, oceano):
        if isinstance(oceano, list):
            self.__oceano_player = oceano
    
    @property
    def oceano_computador(self):
        return self.__oceano_computador
    
    @oceano_computador.setter
    def oceano_computador(self, oceano):
        if isinstance(oceano, list):
            self.__oceano_computador = oceano
    
    @property
    def posicoes_navios_player(self):
        return self.__posicoes_navios_player
    
    @posicoes_navios_player.setter
    def posicoes_navios_player(self, posicoes):
        if isinstance(posicoes, list):
            self.__posicoes_navios_player = posicoes
    
    @property
    def posicoes_navios_computador(self):
        return self.__posicoes_navios_computador
    
    @posicoes_navios_computador.setter
    def posicoes_navios_computador(self, posicoes):
        if isinstance(posicoes, list):
            self.__posicoes_navios_computador = posicoes