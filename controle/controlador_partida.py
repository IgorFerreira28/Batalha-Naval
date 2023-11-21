from limite.tela_partida import TelaPartida
from entidade.partida import Partida
from entidade.jogador import Jogador
from entidade.oceano import Oceano
from limite.tela_oceano import TelaOceano
from limite.tela_jogador import TelaJogador
from random import randrange , randint

class ControladorPartida:
    def __init__(self, controlador_geral):
        self.__jogador = Jogador("a", "1", "1000")
        self.__partida = Partida(self.__jogador)
        self.__tela_partida = TelaPartida()
        self.__controlador_geral = controlador_geral
        self.__tela_oceano = TelaOceano()
        self.__tamanho = 10
        self.__jogadas_player = []
        self.__jogadas_computador = []
        self.__score_player = 0
        self.__score_computador = 0
        self.__oceano_player = Oceano(10)
        self.__oceano_computador = Oceano(10)
        self.__posicoes_navios_player = self.__oceano_player.posicoes_navios
        self.__posicoes_navios_computador  = self.__oceano_computador.posicoes_navios
        self.__oceano_modelo = []

    @property
    def jogador(self):
        return self.__jogador
    
    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador

    @property
    def partida(self):
        return self.__partida
    
    @partida.setter
    def partida(self, partida):
        self.__partida = partida

    @property
    def tela_partida(self):
        return self.__tela_partida

    @property
    def tela_oceano(self):
        return self.__tela_oceano

    @property
    def score_player(self):
        return self.__score_player

    @score_player.setter
    def score_player(self, score):
        self.__score_player = score

    @property
    def score_computador(self):
        return self.__score_computador

    @score_computador.setter
    def score_computador(self, score):
        self.__score_computador = score

    @property
    def oceano_player(self):
        return self.__oceano_player

    @oceano_player.setter
    def oceano_player(self, oceano):
        self.__oceano_player = oceano

    @property
    def oceano_computador(self):
        return self.__oceano_computador

    @oceano_computador.setter
    def oceano_computador(self, oceano):
        self.__oceano_computador = oceano

    @property
    def posicoes_navios_player(self):
        return self.__posicoes_navios_player

    @posicoes_navios_player.setter
    def posicoes_navios_player(self, posicoes):
        self.__posicoes_navios_player = posicoes

    @property
    def jogadas_player(self):
        return self.__jogadas_player

    @jogadas_player.setter
    def jogadas_player(self, jogadas):
        self.__jogadas_player = jogadas

    @property
    def jogadas_computador(self):
        return self.__jogadas_computador

    @jogadas_computador.setter
    def jogadas_computador(self, jogadas):
        self.__jogadas_computador = jogadas

    @property
    def posicoes_navios_computador(self):
        return self.__posicoes_navios_computador

    @posicoes_navios_computador.setter
    def posicoes_navios_computador(self, posicoes):
        self.__posicoes_navios_computador = posicoes

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

    @property
    def oceano_modelo(self):
        return self.__oceano_modelo

    @oceano_modelo.setter
    def oceano_modelo(self, oceano):
        self.__oceano_modelo = oceano

    def comecar_partida(self):
        info = self.__tela_partida.comecar_partida(self.__controlador_geral.controlador_jogador.lista_jogadores)
        self.__jogador = self.__controlador_geral.controlador_jogador.pega_jogador_por_id(info["id"])
        tamanho_oceano = int(info["tamanho_oceano"])
        self.__tamanho = tamanho_oceano
        if isinstance(self.__jogador, Jogador) and isinstance(tamanho_oceano, int):
            self.__partida = Partida(self.__jogador)
            self.__oceano_player = Oceano(tamanho_oceano)
            self.__oceano_computador = Oceano(tamanho_oceano)
            self.__oceano_modelo = [[0] * tamanho_oceano for j in range(tamanho_oceano)]
            self.posiciona_navios(self.__partida.navios_player, self.__partida.navios_computador)
            self.__controlador_geral.cadastra_oceano()

    def navio_player(self):
        return self.__partida.navios_player()

    def navio_computador(self):
        return self.__partida.navios_computador()

    def pontuacao(self, score):
        self.__jogador.pontuacao += score

    def retornar(self):
        self.__controlador_geral.controlador_jogador.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.comecar_partida, 0: self.retornar}

        while True:
            try:
                opcao_escolhida = self.__tela_partida.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
                raise ValueError
            except ValueError:
                self.__tela_partida.mostra_mensagem("Valor inválido, digite um número Válido")

    def abre_tela_oceano(self):
        lista_opcoes = {1: self.jogada, 2:self.mostrar_jogadas, 3:self.mostrar_oceano}

        while True:
            try:
                opcao_escolhida = self.__tela_oceano.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
                raise ValueError
            except ValueError:
                self.__tela_partida.mostra_mensagem("Valor inválido, digite um número Válido")

    def jogada(self):
        tiro_player = True
        tiro_bot = False
        while tiro_player:
            if self.score_player == 41:
                self.tela_oceano.mostra_mensagem("Você Venceu a batalha, Parabéns")
                self.pontuacao(self.score_player)
                dados = [self.oceano_player.mapa, self.oceano_modelo, True, self.tamanho]
                self.__jogador.partidas.append(dados)
                self.__jogadas_computador = []
                self.__jogadas_player = []
                self.__posicoes_navios_computador = []
                self.__posicoes_navios_player = []
                self.__score_computador = 0
                self.__score_player = 0
                self.__controlador_geral.controlador_jogador.abre_tela()
            jogada = self.tela_oceano.jogada()
            tiro = list(jogada)
            if tiro in self.jogadas_player:
                self.tela_oceano.mostra_mensagem("Você já atirou nessa posição")
            else:
                acertou = False
                for j in self.posicoes_navios_computador:
                    if tiro in j:
                        self.__score_player += 1
                        self.oceano_modelo[tiro[0]][tiro[1]] = self.oceano_computador.mapa[tiro[0]][tiro[1]]
                        self.jogadas_player.append(tiro)
                        acertou = True
                        j[0] = j[0] - 1
                        if j[0] == 0:
                            self.__score_player += 3
                            self.tela_oceano.mostra_mensagem("Você destruiu uma embarcação adversária!! +3pts")
                        break
                if acertou:
                    self.tela_oceano.mostra_mensagem("Você acertou uma embarcação, jogue novamente")
                else:
                    tiro_player = False
                    tiro_bot = True
                    self.oceano_modelo[tiro[0]][tiro[1]] = 1
                    self.tela_oceano.mostra_mensagem("Você errou o alvo, espere sua próxima tentativa")
                    self.jogadas_player.append(tiro)

        while tiro_bot:
            if self.score_computador == 41:
                self.pontuacao(self.score_player)
                self.tela_oceano.mostra_mensagem("Você Perdeu a Batalha!")
                dados = list(self.oceano_player.mapa, self.oceano_modelo, False)
                self.__jogador.partidas.append(dados)
                self.__jogadas_computador = []
                self.__jogadas_player = []
                self.__posicoes_navios_computador = []
                self.__posicoes_navios_player = []
                self.__score_computador = 0
                self.__score_player = 0
                self.__controlador_geral.controlador_jogador.abre_tela()
            shot_y = randrange(self.__tamanho)
            shot_x = randrange(self.__tamanho)
            tiro_npc = [shot_y, shot_x]
            if tiro_npc in self.jogadas_computador:
                continue
            else:
                acertou = False
                for j in self.posicoes_navios_player:
                    if tiro_npc in j:
                        self.__score_computador += 1
                        self.jogadas_computador.append(tiro_npc)
                        acertou = True
                        self.oceano_player.mapa[tiro_npc[0]][tiro_npc[1]] = 'X'
                        j[0] = j[0] - 1
                        if j[0] == 0:
                            self.__score_computador += 3
                            self.tela_oceano.mostra_mensagem("O Computador destruiu uma embarcação sua")
                        break
                if acertou:
                    self.tela_oceano.mostra_mensagem("O Computador acertou sua embarcação")
                else:
                    tiro_bot = False
                    self.oceano_player.mapa[tiro_npc[0]][tiro_npc[1]] = 1
                    self.jogadas_computador.append(tiro_npc)
                    self.tela_oceano.mostra_mensagem("O Computador errou, agora é sua vez")


    def mostrar_jogadas(self):
        self.tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_modelo)

    def mostrar_oceano(self):
        self.tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_player.mapa)

    def posiciona_navios(self, barco_player, barco_bot):
        for barco in barco_player:
            tipo_navio = barco.__class__.__name__
            self.posicionar_navio(tipo_navio, "player")
        
        for barco in barco_bot:
            tipo_navio = barco.__class__.__name__
            self.posicionar_navio(tipo_navio, "computador")
    
    def posicionar_navio(self, tipo_navio, jogador):
        if tipo_navio == "Bote":
            self.posiciona_bote(jogador)
        elif tipo_navio == "Fragata":
            self.posiciona_fragata(3, jogador)
        elif tipo_navio == "PortaAvioes":
            self.posiciona_porta_avioes(4, jogador)
        elif tipo_navio == "Submarino":
            self.posiciona_submarino(2, jogador)

    def posiciona_bote(self, who):
        if who == "player":
            self.tela_oceano.mostra_mensagem("Posicinando um Bote: 1 Posicao")
            lista_temporaria = [1]
            while True:
                coordenada = self.tela_oceano.posiciona_navios()
                posicao = list(coordenada)
                posicao_em_uso = False
                for i in self.posicoes_navios_player:
                    if posicao in i:
                        posicao_em_uso = True
                    if posicao_em_uso:
                        self.tela_oceano.mostra_mensagem("Está posição já está ocupada!")
                if not posicao_em_uso:
                    lista_temporaria.append(posicao)
                    self.__posicoes_navios_player.append(lista_temporaria)
                    self.__oceano_player.mapa[posicao[0]][posicao[1]] = 'B'
                    self.tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_player.mapa)
                    break

        elif who == "computador":
            lista_temporaria = [1]
            while True:
                posicao = [randint(0, self.__tamanho - 1), randint(0, self.__tamanho - 1)]
                posicao_em_uso = False
                for i in self.__posicoes_navios_computador:
                    if posicao in i:
                        posicao_em_uso = True
                        break
                if not posicao_em_uso:
                    lista_temporaria.append(posicao)
                    self.__posicoes_navios_computador.append(lista_temporaria)
                    self.__oceano_computador.mapa[posicao[0]][posicao[1]] = 'B'
                    break

    def posiciona_porta_avioes(self, tamanho, who):
        if who == "player":
            self.tela_oceano.mostra_mensagem("Posicionando um Porta-Aviões: 4 Posições")
            porta_avioes_restantes = 1

            while porta_avioes_restantes > 0:
                condicaox = True
                condicaoy = True
                try:
                    posicoes_x = self.tela_oceano.posiciona_navios_x()
                    posicoes_y = self.tela_oceano.posiciona_navios_y()

                    if len(posicoes_x) == tamanho and len(posicoes_y) == 1:
                        condicaoy = False
                    
                    elif len(posicoes_y) == tamanho and len(posicoes_x) == 1:
                        condicaox = False

                    else:
                        self.tela_oceano.mostra_mensagem(f"Por favor, insira {tamanho} coordenadas para um dos eixos e 1 para o outro para inserir uma Fragata.")
                        continue

                    positions = []

                    if condicaox:
                        positions = [[posicoes_y[0], x] for x in posicoes_x]
                    elif condicaoy:
                        positions = [[y, posicoes_x[0]] for y in posicoes_y]

                    if any(self.__oceano_player.mapa[position[0]][position[1]] != 0 for position in positions):
                        self.tela_oceano.mostra_mensagem("Você colocou uma posição já em uso, posicione novamente")
                        continue

                    lista_temporaria = [tamanho] + positions
                    self.__posicoes_navios_player.append(lista_temporaria)

                    for position in positions:
                        self.__oceano_player.mapa[position[0]][position[1]] = 'P'

                    self.tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_player.mapa)
                    porta_avioes_restantes -= 1

                except ValueError:
                    self.tela_oceano.mostra_mensagem("Por favor, insira coordenadas válidas (números inteiros).")
        elif who == "computador":
            lista_temporaria = [4]
            while True:
                posicao_x, posicao_y = randint(0, self.__tamanho - tamanho), randint(0, self.__tamanho - 1)
                condicao = True
                for i in range(tamanho):
                    if not (0 <= posicao_x + i < self.__tamanho) or not (0 <= posicao_y < self.__tamanho) or \
                            self.__oceano_computador.mapa[posicao_y][posicao_x + i] != 0:
                        condicao = False
                        break
                if condicao:
                    for i in range(tamanho):
                        lista_temporaria.append([posicao_y, posicao_x + i])
                        self.__oceano_computador.mapa[posicao_y][posicao_x + i] = 'P'
                    self.__posicoes_navios_computador.append(lista_temporaria)
                    break
            
    def posiciona_fragata(self, tamanho, who):
        if who == "player":
            self.tela_oceano.mostra_mensagem("Posicionando uma Fragata: 3 Posições")
            fragatas_restantes = 1
            while fragatas_restantes > 0:
                condicaox = True
                condicaoy = True
                try:
                    posicoes_x = self.tela_oceano.posiciona_navios_x()
                    posicoes_y = self.tela_oceano.posiciona_navios_y()

                    if len(posicoes_x) == tamanho and len(posicoes_y) == 1:
                        condicaoy = False
                    
                    elif len(posicoes_y) == tamanho and len(posicoes_x) == 1:
                        condicaox = False

                    else:
                        self.tela_oceano.mostra_mensagem(f"Por favor, insira {tamanho} coordenadas para um dos eixos e 1 para o outro para inserir uma Fragata.")
                        continue

                    positions = []

                    if condicaox:
                        positions = [[posicoes_y[0], x] for x in posicoes_x]
                    elif condicaoy:
                        positions = [[y, posicoes_x[0]] for y in posicoes_y]

                    if any(self.__oceano_player.mapa[position[0]][position[1]] != 0 for position in positions):
                        self.tela_oceano.mostra_mensagem("Você colocou uma posição já em uso, posicione novamente")
                        continue

                    lista_temporaria = [tamanho] + positions
                    self.__posicoes_navios_player.append(lista_temporaria)

                    for position in positions:
                        self.__oceano_player.mapa[position[0]][position[1]] = 'F'

                    self.tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_player.mapa)
                    fragatas_restantes -= 1

                except ValueError:
                    self.tela_oceano.mostra_mensagem("Por favor, insira coordenadas válidas (números inteiros).")
                                
        elif who == "computador":
            lista_temporaria = [3]
            while True:
                posicao_x, posicao_y = randint(0, self.__tamanho - 3), randint(0, self.__tamanho - 1)
                condicao = True
                for i in range(3):
                    if not (0 <= posicao_x + i < self.__tamanho) or not (0 <= posicao_y < self.__tamanho) or \
                            self.__oceano_computador.mapa[posicao_y][posicao_x + i] != 0:
                        condicao = False
                        break
                if condicao:
                    for i in range(3):
                        lista_temporaria.append([posicao_y, posicao_x + i])
                        self.__oceano_computador.mapa[posicao_y][posicao_x + i] = 'F'
                    self.__posicoes_navios_computador.append(lista_temporaria)
                    break

    def posiciona_submarino(self, tamanho, who):
        if who == "player":
            self.tela_oceano.mostra_mensagem(f"Posicionando um Submarino: {tamanho} Posições")
            submarinos_restantes = 1

            while submarinos_restantes > 0:
                condicaox = True
                condicaoy = True
                try:
                    posicoes_x = self.tela_oceano.posiciona_navios_x()
                    posicoes_y = self.tela_oceano.posiciona_navios_y()

                    if len(posicoes_x) == tamanho and len(posicoes_y) == 1:
                        condicaoy = False
                    
                    elif len(posicoes_y) == tamanho and len(posicoes_x) == 1:
                        condicaox = False

                    else:
                        self.tela_oceano.mostra_mensagem(f"Por favor, insira {tamanho} coordenadas para um dos eixos e 1 para o outro para inserir uma Fragata.")
                        continue

                    positions = []

                    if condicaox:
                        positions = [[posicoes_y[0], x] for x in posicoes_x]
                    elif condicaoy:
                        positions = [[y, posicoes_x[0]] for y in posicoes_y]

                    if any(self.__oceano_player.mapa[position[0]][position[1]] != 0 for position in positions):
                        self.tela_oceano.mostra_mensagem("Você colocou uma posição já em uso, posicione novamente")
                        continue

                    lista_temporaria = [tamanho] + positions
                    self.__posicoes_navios_player.append(lista_temporaria)

                    for position in positions:
                        self.__oceano_player.mapa[position[0]][position[1]] = 'S'

                    self.tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_player.mapa)
                    submarinos_restantes -= 1

                except ValueError:
                    self.tela_oceano.mostra_mensagem("Por favor, insira coordenadas válidas (números inteiros).")

        elif who == "computador":
            lista_temporaria = [2]
            while True:
                posicao_x, posicao_y = randint(0, self.__tamanho - 2), randint(0, self.__tamanho - 1)
                condicao = True
                for i in range(2):
                    if not (0 <= posicao_x + i < self.__tamanho) or not (0 <= posicao_y < self.__tamanho) or \
                            self.__oceano_computador.mapa[posicao_y][posicao_x + i] != 0:
                        condicao = False
                        break
                if condicao:
                    for i in range(2):
                        lista_temporaria.append([posicao_y, posicao_x + i])
                        self.__oceano_computador.mapa[posicao_y][posicao_x + i] = 'S'
                    self.__posicoes_navios_computador.append(lista_temporaria)
                    break
            self.tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_computador.mapa)
