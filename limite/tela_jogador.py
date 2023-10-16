class TelaJogador():
  def tela_opcoes(self):
    print("-------- Tela Jogador --------")
    print("Escolha uma opçâo")
    print("1 - Incluir Jogador")
    print("2 - Alterar Jogador")
    print("3 - Listar Jogadores")
    print("4 - Mostrar Histórico")
    print("5 - Mostrar Ranking dos jogadores")
    print("6 - Seção de Partida")
    print("7 - Excluir ")
    print("0 - Retornar")

    opcao = int(input("Escolha a opção: "))
    return opcao
  
  def dados_jogador(self):
    print("-------- DADOS JOGADOR ----------")
    while True:
        try:
            nome = input("Nome: ")
            if not nome:
                raise ValueError("O nome não pode ser vazio.")
            
            data_nascimento = input("Data de nascimento: ")
            if not data_nascimento:
                raise ValueError("A data de nascimento não pode ser vazia.")
            
            id = input("ID: ")
            if not id:
                raise ValueError("O ID não pode ser vazio.")
            
            return {"nome": nome, "data_nascimento": data_nascimento, "id": id}
        except ValueError as ve:
            print(f"Erro: {ve}. Por favor, tente novamente.")


  def seleciona_jogador(self):
    try:
      id = input('Digite o ID do jogador que deseja selecionar: ')
      if not id:
         raise ValueError("O ID não pode ser vazio.")
      return id
    except ValueError as ve:
       print(f"Erro: {ve}. Por favor, tente novamente.")
  
  def mostra_jogador(self, dados_jogador):
    print("NOME DO JOGADOR: ", dados_jogador["nome"])
    print("NASCIMENTO DO JOGADOR: ", dados_jogador["data_nascimento"])
    print("ID DO JOGADOR: ", dados_jogador["id"])
    print("\n")

  def seleciona_partida(self):
    try:
      num = int(input("Selecione um número entre as opções: "))
      if not num:
         raise ValueError("O Número não pode ser vazio.")
      if isinstance(num, str):
         raise ValueError("O Número deve ser um número.")
      return id
    except ValueError as ve:
       print(f"Erro: {ve}. Por favor, tente novamente.")
    num = int(input("Selecione um número entre as opções: "))
    return num - 1 

  def mostra_rank(self, rank):
    print(rank)
  
  def mostra_mensagem(self, msg):
    print(msg)