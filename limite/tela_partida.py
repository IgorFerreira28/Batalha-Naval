class TelaPartida:
    def tela_opcoes(self):
        print("-------- Tela Partida --------")
        print("Escolha uma opção")
        print("1 - Começar Partida")
        print("0 - Retornar")

        opcao = int(input("Selecione uma opção "))
        return opcao
    
    def comecar_partida(self):
        print("-------- Início Partida --------")
        id = int(input("Digite o ID do jogador que jogará está partida: "))
        tamanho_oceano = int(input("Tamanho do oceano: "))

        return {"id": id, "tamanho_oceano": tamanho_oceano}
    
    def mostra_mensagem(self, msg):
        return msg
