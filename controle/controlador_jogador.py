from limite.tela_jogador import TelaJogador
from entidade.jogador import Jogador
from DAOs.jogador_dao import JogadorDAO

class ControladorJogador:
    def __init__(self, controlador_geral):
        self.__tela_jogador = TelaJogador()
        self.__controlador_geral = controlador_geral
        self.__jogador_DAO = JogadorDAO()

    @property
    def jogador_DAO(self):
        return self.__jogador_DAO
    
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
        for jogador in self.__jogador_DAO.get_all():
            if(jogador.id == id):
                return jogador
        return None

    def inserir_jogador(self):
        dados_jogador = self.tela_jogador.dados_jogador()
        livre = True
        for i in self.__jogador_DAO.get_all():
            if i.id == dados_jogador["id"]:
                livre = False
                self.tela_jogador.mostra_mensagem("Esse ID ja esta em uso!")
        if livre:
            player = Jogador(dados_jogador["nome"], dados_jogador["data_nascimento"], dados_jogador["id"])
            self.__jogador_DAO.add(player)

    def alterar_jogador(self):
        id_jogador = self.tela_jogador.seleciona_jogador(self.__jogador_DAO.get_all())
        player = self.pega_jogador_por_id(id_jogador)
        livre = True
        if (player is not None):
            novo_player = self.tela_jogador.dados_jogador()
            for i in self.__jogador_DAO.get_all():
                if i.id == novo_player["id"]:
                    self.tela_jogador.mostra_mensagem("ID ja em uso!")
                    livre = False
            if livre:
                player.nome = novo_player["nome"]
                player.data_nascimento = novo_player["data_nascimento"]
                player.id = novo_player["id"]
                self.__jogador_DAO.update(player)

    def listar_jogadores(self):
        dados_jogadores = [
            {"nome": jogador.nome, "data_nascimento": jogador.data_nascimento, "id": jogador.id}
            for jogador in self.__jogador_DAO.get_all()
        ]
        self.tela_jogador.mostra_jogador(dados_jogadores)

    def historico_partidas(self):
        id_jogador = self.tela_jogador.seleciona_jogador(self.__jogador_DAO.get_all())
        jogador = self.pega_jogador_por_id(id_jogador)

        if jogador is not None:
            self.tela_jogador.mostra_mensagem(f"O {jogador.nome}, tem {len(jogador.partidas)} partidas em seu histórico")

            if len(jogador.partidas) == 0:
                self.abre_tela()

            partidas = [f"Partida Número {i + 1}" for i in range(len(jogador.partidas))]
            selected_partida = self.tela_jogador.seleciona_partida(partidas)

            if selected_partida is not None:
                num = int(selected_partida.split()[-1])

                self.tela_jogador.mostra_mensagem("---- Oceano do Jogador ----")
                self.tela_jogador.mostra_historico(jogador.partidas[num - 1][3], jogador.partidas[num - 1][0])

                self.tela_jogador.mostra_mensagem("---- Jogadas Realizadas ----")
                self.tela_jogador.mostra_historico(jogador.partidas[num - 1][3], jogador.partidas[num - 1][1])

                if jogador.partidas[num - 1][2]:
                    self.tela_jogador.mostra_mensagem(f"O {jogador.nome} venceu a partida")
                else:
                    self.tela_jogador.mostra_mensagem(f"O {jogador.nome} perdeu a partida")

    def secao_partida(self):
        self.__controlador_geral.cadastra_partida()

    def deletar_jogador(self):
        id_jogador = self.tela_jogador.seleciona_jogador(self.__jogador_DAO.get_all()) 
        jogador = self.pega_jogador_por_id(id_jogador)
        if jogador is not None:
            self.__jogador_DAO.remove(jogador)

    def get_rank(self):
        players = self.__jogador_DAO.get_all()
        players.sort(key=lambda player: player.pontuacao, reverse=True)
        rank_info = [(i+1, player.nome, player.pontuacao) for i, player in enumerate(players)]
        self.tela_jogador.mostra_rank(rank_info)

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
