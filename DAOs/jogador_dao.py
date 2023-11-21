from DAOs.dao import DAO
from entidade.jogador import Jogador


class JogadorDAO(DAO):
    def __init__(self):
        super().__init__('jogador.pkl')

    def add(self, jogador: Jogador):
        if (jogador is not None) and isinstance(jogador, Jogador) and isinstance(jogador.id, int):
            super().add(jogador.id, jogador)

    def update(self, jogador: Jogador):
        if (jogador is not None) and isinstance(jogador, Jogador) and isinstance(jogador.id, int):
            super().update(jogador.id, jogador)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)
    #def __init__(self):
    #    super().__init__('jogador.pkl')

    #def add(self, jogador: Jogador):
    #    if((jogador is not None) and isinstance(jogador, Jogador) and isinstance(jogador.id, int)):
    #        super().add(jogador.id, jogador)

    #def update(self, jogador: Jogador):
    #    if((jogador is not None) and isinstance(jogador, Jogador) and isinstance(jogador.id, int)):
    #        super().update(jogador.id, jogador)

    #def get(self, key:int):
    #    if isinstance(key, int):
    #        return super().get(key)

    #def remove(selfself, key:int):
    #    if(isinstance(key, int)):
    #       return super().remove(key)