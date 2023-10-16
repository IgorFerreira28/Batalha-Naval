from abc import ABC, abstractmethod

class Embarcacoes(ABC):
    def __init__(self, tamanho):
        self.__tamanho = tamanho

    @property
    @abstractmethod
    def tamanho(self):
        return self.__tamanho