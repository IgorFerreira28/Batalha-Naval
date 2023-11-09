class Jogador:
    def __init__(self, nome, data_nascimento, id):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__id = id
        self.__pontuacao = 0
        self.__partidas = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def pontuacao(self):
        return self.__pontuacao
    
    @pontuacao.setter
    def pontuacao(self, pontuacao):
        self.__pontuacao = pontuacao
    
    @property
    def partidas(self):
        return self.__partidas