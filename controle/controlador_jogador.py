from limite.tela_jogador import TelaJogador
from entidade.jogador import Jogador

class ControladorJogador:
    def __init__(self, controlador_geral):
        self.__lista_jogadores = []
        self.__tela_jogador = TelaJogador()
        self.__controlador_geral = controlador_geral

    @property
    def lista_jogadores(self):
        return self.__lista_jogadores
    
    @lista_jogadores.setter
    def lista_jogadores(self, lista):
        if isinstance(lista, list):
            self.__lista_jogadores = lista

    @property
    def tela_jogador(self):
        return self.__tela_jogador

    @tela_jogador.setter
    def tela_jogador(self, tela):
        if isinstance(tela, TelaJogador):
            self.__tela_jogador = tela

    @property
    def controlador_geral(self):
        return self.__controlador_geral
    
    def pega_jogador_por_id(self, id):
        for jogador in self.lista_jogadores:
            if(jogador.id == id):
                return jogador
        return None

    def inserir_jogador(self):
        dados_jogador = self.tela_jogador.dados_jogador()
        player = Jogador(dados_jogador["nome"], dados_jogador["data_nascimento"], dados_jogador["id"])
        self.lista_jogadores.append(player)

    def alterar_jogador(self):
        self.listar_jogadores()
        id_jogador = self.tela_jogador.seleciona_jogador()
        player = self.pega_jogador_por_id(id_jogador)

        if (player is not None):
            novo_player = self.tela_jogador.dados_jogador()
            player.nome = novo_player["nome"]
            player.data_nascimento = novo_player["data_nascimento"]
            player.id = novo_player["id"]
        else:
            self.tela_jogador.mostra_mensagem("ATENÇÃO: Esse Jogador Não Existe")

    def listar_jogadores(self):
        for jogador in self.lista_jogadores:
            self.tela_jogador.mostra_jogador({"nome": jogador.nome, "data_nascimento": jogador.data_nascimento, "id": jogador.id})

    def historico_partidas(self):
        self.listar_jogadores()
        id_jogador = self.tela_jogador.seleciona_jogador() 
        jogador = self.pega_jogador_por_id(id_jogador)
        if jogador is not None:
            self.tela_jogador.mostra_mensagem(f"O {jogador.nome()}, tem {len(jogador.partidas())} partidas em seu histórico")
            for i in range(len(jogador.partidas)):
                self.tela_jogador.mostra_mensagem(f"Partida Número {i+1}")
            num = self.tela_jogador.seleciona_partida()
            self.tela_jogador.mostra_mensagem(f"{jogador.partidas()[num-1]}")

    def secao_partida(self):
        self.__controlador_geral.cadastra_partida()

    def deletar_jogador(self):
        self.listar_jogadores()
        id_jogador = self.tela_jogador.seleciona_jogador() 
        jogador = self.pega_jogador_por_id(id_jogador)
        if jogador is not None:
            self.lista_jogadores.remove(jogador)
        else:
            self.tela_jogador.mostra_mensagem("Esse Jogador Não Existe Para Ser Apagado!")

    def get_rank(self):
        players = self.lista_jogadores
        players.sort(key=lambda players: players.pontuacao)
        
        for i in range(len(players)):
            self.tela_jogador.mostra_rank(f'{i+1}º - {players.nome} Pontuação: {players.pontuacao}')

    def retornar(self):
        self.controlador_geral.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.inserir_jogador, 2: self.alterar_jogador, 3: self.listar_jogadores, 4: self.historico_partidas, 5: self.get_rank, 6: self.secao_partida, 7: self.deletar_jogador, 0: self.retornar}

        continua = True
        while continua:
            try:
                opcao = self.tela_jogador.tela_opcoes()
                if opcao in lista_opcoes:
                    lista_opcoes[opcao]()
                else:
                    self.__tela_jogador.mostra_mensagem("Opção inválida. Por favor, escolha uma opção válida.")
            except Exception as e:
                self.__tela_jogador.mostra_mensagem(f"Ocorreu um erro: {e}")

