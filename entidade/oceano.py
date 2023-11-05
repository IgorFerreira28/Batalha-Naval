class Oceano:
    def __init__(self, tamanho_oceano):
        self.__tamanho_oceano = tamanho_oceano
        self.__posicoes_navios = []
        self.__mapa = [[0] * self.__tamanho_oceano for j in range(self.__tamanho_oceano)]

    @property
    def tamanho_oceano(self):
        return self.__tamanho_oceano
    
    @tamanho_oceano.setter
    def tamanho_oceano(self, tamanho):
        if isinstance(tamanho, int):
            self.__tamanho_oceano = tamanho

    @property
    def mapa(self):
        return self.__mapa
    
    @mapa.setter
    def mapa(self, oceano):
        if isinstance(oceano, list):
            self.__mapa = oceano

    @property
    def posicoes_navios(self):
        return self.__posicoes_navios
    
    @posicoes_navios.setter
    def posicoes_navios(self, posicoes):
        if isinstance(posicoes, list):
            self.__posicoes_navios = posicoes
