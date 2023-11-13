from limite.tela_partida import TelaPartida
from entidade.partida import Partida
from entidade.jogador import Jogador
from entidade.oceano import Oceano
from limite.tela_oceano import TelaOceano
from limite.tela_jogador import TelaJogador
from random import randrange

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
        info = self.__tela_partida.comecar_partida()
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

    def partida(self):
        return self.__partida

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
        barcos_player = barco_player
        barcos_computador = barco_bot
        for boat in barcos_player:
            if boat.__class__.__name__ == "Bote":  
                self.posiciona_bote("player")
            elif boat.__class__.__name__ == "Fragata":
                self.posiciona_fragata(3 , "player")
            elif boat.__class__.__name__ == "PortaAvioes":
                self.posiciona_porta_avioes(4, "player")
            elif boat.__class__.__name__ == "Submarino":
                self.posiciona_submarino( 2 , "player")

        for boat in barcos_computador:
            bote = 0
            fragata = 0
            submarino = 0
            porta_avioes = 0
            if boat.__class__.__name__ == "Bote" and bote == 0:
                self.posiciona_bote("computador")
                bote += 1
            elif boat.__class__.__name__ == "Fragata" and fragata == 0:
                self.posiciona_fragata( 3, "computador")
                fragata += 1
            elif boat.__class__.__name__ == "PortaAvioes" and porta_avioes == 0:
                self.posiciona_porta_avioes(4, "computador")
                porta_avioes += 1
            elif boat.__class__.__name__ == "Submarino" and submarino == 0:
                self.posiciona_submarino( 2, "computador")
                submarino += 1

    def posiciona_bote(self, who):
        self.tela_oceano.mostra_mensagem("Posicinando um Bote: 1 Posicao")
        lista_temporaria = [1]
        if who == "player":
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
            lista_temporaria1 = [1, [2,3]]
            lista_temporaria2 = [1, [8,0]]
            lista_temporaria3 = [1, [5,3]]
            self.__oceano_computador.mapa[2][3] = 'B'
            self.__oceano_computador.mapa[8][0] = 'B'
            self.__oceano_computador.mapa[5][3] = 'B'
            self.__posicoes_navios_computador.append(lista_temporaria1)
            self.__posicoes_navios_computador.append(lista_temporaria2)
            self.__posicoes_navios_computador.append(lista_temporaria3)

    def posiciona_porta_avioes(self, tamanho, who):
        self.tela_oceano.mostra_mensagem("Posicinando um Porta Aviões: 4 Posicões")
        lista_temporaria = [4] 
        if who == "player":
            porta_avioes_restantes = 1
            while porta_avioes_restantes > 0:
                condicaox = True
                condicaoy = True
                try:
                    posicoes_x = self.tela_oceano.posiciona_navios_x()
                    posicoes_y = self.tela_oceano.posiciona_navios_y()

                    if len(posicoes_x) == 4 and len(posicoes_y) == 1:
                        condicaoy = False
                        if any(x < 0 or x >= self.__tamanho for x in posicoes_x) or posicoes_y[0] < 0 or posicoes_y[0] >= self.__tamanho:
                            self.tela_oceano.mostra_mensagem("Posição inválida, por favor insira novamente.")
                            condicaox = False
                            continue
                        else:
                            for x in posicoes_x:
                                position = [posicoes_y[0], x]
                                for i in self.posicoes_navios_player:
                                    if position in i:
                                        self.tela_oceano.mostra_mensagem("Você colocou uma posição já em uso, posicione novamente")
                                        condicaox = False
                                        continue
                    elif len(posicoes_y) == 4 and len(posicoes_x) == 1:
                        condicaox = False
                        if any(y < 0 or y >= self.__tamanho for y in posicoes_y) or posicoes_x[0] < 0 or posicoes_x[0] >= self.__tamanho:
                            self.tela_oceano.mostra_mensagem("Posição inválida, por favor insira novamente.")
                            condicaoy = False
                            continue
                        else:
                            for y in posicoes_y:
                                position = [y, posicoes_x[0]]
                                for i in self.posicoes_navios_player:
                                    if position in i:
                                        self.tela_oceano.mostra_mensagem("Você colocou uma posição já em uso, posicione novamente")
                                        condicaoy = False
                                        continue
                    else:
                        self.tela_oceano.mostra_mensagem("Por favor, insira 4 coordenadas para Y e 1 para X ou vice-versa para inserir uma Fragata.")
                        continue
                        
                    if condicaox:
                        for x in posicoes_x:
                            lista_temporaria.append([posicoes_y[0], x]) 
                            self.__posicoes_navios_player.append(lista_temporaria)
                            self.__oceano_player.mapa[posicoes_y[0]][x] = 'P'
                        self.tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_player.mapa)
                        porta_avioes_restantes -= 1
                    elif condicaoy:
                        for y in posicoes_y:
                            lista_temporaria.append([posicoes_x[0], y])
                            self.__posicoes_navios_player.append(lista_temporaria)
                            self.__oceano_player.mapa[y][posicoes_x[0]] = 'P'
                        self.tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_player.mapa)
                        porta_avioes_restantes -= 1

                except ValueError:
                    self.tela_oceano.mostra_mensagem("Por favor, insira coordenadas válidas (números inteiros).")
        
        elif who == "computador":
            lista_temporaria = [4,[0,0],[0,1],[0,2],[0,3]]
            self.__oceano_computador.mapa[0][0] = 'P'
            self.__oceano_computador.mapa[0][1] = 'P'
            self.__oceano_computador.mapa[0][2] = 'P'
            self.__oceano_computador.mapa[0][3] = 'P'
            self.__posicoes_navios_computador.append(lista_temporaria)
            
    def posiciona_fragata(self, tamanho, who):
        self.tela_oceano.mostra_mensagem("Posicinando uma Fragata: 3 Posicões")
        lista_temporaria = [3] 
        if who == "player":
            fragatas_restantes = 1
            while fragatas_restantes > 0:
                condicaox = True
                condicaoy = True
                try:
                    posicoes_x = self.tela_oceano.posiciona_navios_x()
                    posicoes_y = self.tela_oceano.posiciona_navios_y()

                    if len(posicoes_x) == 3 and len(posicoes_y) == 1:
                        condicaoy = False
                        if any(x < 0 or x >= self.__tamanho for x in posicoes_x) or posicoes_y[0] < 0 or posicoes_y[0] >= self.__tamanho:
                            self.tela_oceano.mostra_mensagem("Posição inválida, por favor insira novamente.")
                            condicaox = False
                            continue
                        else:
                            for x in posicoes_x:
                                position = [posicoes_y[0], x]
                                for i in self.posicoes_navios_player:
                                    if position in i:
                                        self.tela_oceano.mostra_mensagem("Você colocou uma posição já em uso, posicione novamente")
                                        condicaox = False
                                        continue
                    elif len(posicoes_y) == 3 and len(posicoes_x) == 1:
                        condicaox = False
                        if any(y < 0 or y >= self.__tamanho for y in posicoes_y) or posicoes_x[0] < 0 or posicoes_x[0] >= self.__tamanho:
                            self.tela_oceano.mostra_mensagem("Posição inválida, por favor insira novamente.")
                            condicaoy = False
                            continue
                        else:
                            for y in posicoes_y:
                                position = [y, posicoes_x[0]]
                                for i in self.posicoes_navios_player:
                                    if position in i:
                                        self.tela_oceano.mostra_mensagem("Você colocou uma posição já em uso, posicione novamente")
                                        condicaoy = False
                                        continue
                    else:
                        self.tela_oceano.mostra_mensagem("Por favor, insira 3 coordenadas para Y e 1 para X para inserir uma Fragata.")
                        continue
                        
                    if condicaox:
                        for x in posicoes_x:
                            lista_temporaria.append([posicoes_y[0], x]) 
                            self.__posicoes_navios_player.append(lista_temporaria)
                            self.__oceano_player.mapa[posicoes_y[0]][x] = 'F'
                        self.tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_player.mapa)
                        fragatas_restantes -= 1
                    elif condicaoy:
                        for y in posicoes_y:
                            lista_temporaria.append([posicoes_x[0], y])
                            self.__posicoes_navios_player.append(lista_temporaria)
                            self.__oceano_player.mapa[y][posicoes_x[0]] = 'F'
                        self.tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_player.mapa)
                        fragatas_restantes -= 1

                except ValueError:
                    self.tela_oceano.mostra_mensagem("Por favor, insira coordenadas válidas (números inteiros).")
                            
        elif who == "computador":
            lista_temporaria1 = [3, [3,5],[3,6],[3,7]]
            lista_temporaria2 =[3, [4,0],[5,0],[6,0]]
            self.__oceano_computador.mapa[3][5]= 'F'
            self.__oceano_computador.mapa[3][6] = 'F'
            self.__oceano_computador.mapa[3][7] = 'F'
            self.__oceano_computador.mapa[4][0] = 'F'
            self.__oceano_computador.mapa[5][0] = 'F'
            self.__oceano_computador.mapa[6][0] = 'F'
            self.__posicoes_navios_computador.append(lista_temporaria1)
            self.__posicoes_navios_computador.append(lista_temporaria2)

    def posiciona_submarino(self, tamanho, who):
        self.tela_oceano.mostra_mensagem("Posicinando um Submarino: 2 Posicões")
        lista_temporaria = [2]
        if who == "player":
            submarinos_restantes = 1
            while submarinos_restantes > 0:
                condicaox = True
                condicaoy = True
                try:
                    posicoes_x = self.tela_oceano.posiciona_navios_x()
                    posicoes_y = self.tela_oceano.posiciona_navios_y()

                    if len(posicoes_x) == 2 and len(posicoes_y) == 1:
                        condicaoy = False
                        if any(x < 0 or x >= self.__tamanho for x in posicoes_x) or posicoes_y[0] < 0 or posicoes_y[0] >= self.__tamanho:
                            self.tela_oceano.mostra_mensagem("Posição inválida, por favor insira novamente.")
                            condicaox = False
                            continue
                        else:
                            for x in posicoes_x:
                                position = [posicoes_y[0], x]
                                for i in self.posicoes_navios_player:
                                    if position in i:
                                        self.tela_oceano.mostra_mensagem("Você colocou uma posição já em uso, posicione novamente")
                                        condicaox = False
                                        continue
                    elif len(posicoes_y) == 2 and len(posicoes_x) == 1:
                        condicaox = False
                        if any(y < 0 or y >= self.__tamanho for y in posicoes_y) or posicoes_x[0] < 0 or posicoes_x[0] >= self.__tamanho:
                            self.tela_oceano.mostra_mensagem("Posição inválida, por favor insira novamente.")
                            condicaoy = False
                            continue
                        else:
                            for y in posicoes_y:
                                position = [y, posicoes_x[0]]
                                for i in self.posicoes_navios_player:
                                    if position in i:
                                        self.tela_oceano.mostra_mensagem("Você colocou uma posição já em uso, posicione novamente")
                                        condicaoy = False
                                        continue
                    else:
                        self.tela_oceano.mostra_mensagem("Por favor, insira 2 coordenadas para Y e 1 para X para inserir uma Fragata.")
                        continue
                        
                    if condicaox:
                        for x in posicoes_x:
                            lista_temporaria.append([posicoes_y[0], x]) 
                            self.__posicoes_navios_player.append(lista_temporaria)
                            self.__oceano_player.mapa[posicoes_y[0]][x] = 'S'
                        self.tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_player.mapa)
                        submarinos_restantes -= 1
                    elif condicaoy:
                        for y in posicoes_y:
                            lista_temporaria.append([posicoes_x[0], y])
                            self.__posicoes_navios_player.append(lista_temporaria)
                            self.__oceano_player.mapa[y][posicoes_x[0]] = 'S'
                        self.tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_player.mapa)
                        submarinos_restantes -= 1

                except ValueError:
                    self.tela_oceano.mostra_mensagem("Por favor, insira coordenadas válidas (números inteiros).")

        elif who == "computador":
            lista_temporaria1 = [2, [6,5],[6,6]]
            lista_temporaria2 = [2, [4,4], [4,5]]
            self.__oceano_computador.mapa[6][5] = 'S'
            self.__oceano_computador.mapa[6][6] = 'S'
            self.__oceano_computador.mapa[4][4] = 'S'
            self.__oceano_computador.mapa[4][5] = 'S'
            self.__posicoes_navios_computador.append(lista_temporaria1)
            self.__posicoes_navios_computador.append(lista_temporaria2)
            self.tela_oceano.mostrar_oceano(self.__tamanho, self.__oceano_computador.mapa)
