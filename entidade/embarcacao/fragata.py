from entidade.embarcacao.abstractEmbarcacoes import Embarcacoes
class Fragata(Embarcacoes):
    def __init__(self, tamanho):
        super().__init__(tamanho)
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

        