import PySimpleGUI as sg

class TelaJogador():
  def __init__(self):
     self.__window = None
     self.init_opcoes()

  def tela_opcoes(self):
    self.init_opcoes()
    button, values = self.open()
    if values['1']:
      opcao = 1
    if values['2']:
      opcao = 2
    if values['3']:
      opcao = 3
    if values['4']:
      opcao = 4
    if values['5']:
       opcao = 5
    if values['6']:
       opcao = 6
    if values['7']:
       opcao = 7
    if values['0'] or button in (None, 'Cancelar'):
      opcao = 0
    self.close()
    return opcao
  
  def init_opcoes(self):
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- Tela Jogador ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Incluir Jogador', "RD1", key='1')],
      [sg.Radio('Alterar Jogador', "RD1", key='2')],
      [sg.Radio('Listar Jogadores', "RD1", key='3')],
      [sg.Radio('Mostrar Histórico', "RD1", key='4')],
      [sg.Radio('Mostrar Ranking dos Jogadores', "RD1", key='5')],
      [sg.Radio('Seção de Partida', "RD1", key='6')]
      [sg.Radio('Excluir Jogador', "RD1", key='7')],
      [sg.Radio('Retornar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de Jogadores').Layout(layout)
  
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
            
            id = int(input("ID: "))
            if not id:
                raise ValueError("O ID não pode ser vazio.")
            
            if isinstance(id, str):
               raise ValueError("O ID deve ser um numero inteiro")
            
            return {"nome": nome, "data_nascimento": data_nascimento, "id": id}
        except ValueError as ve:
            print(f"Erro: {ve}. Por favor, tente novamente.")


  def seleciona_jogador(self):
    try:
      id = int(input('Digite o ID do jogador que deseja selecionar: '))
      if not id:
         raise ValueError("O ID não pode ser vazio.")
      
      if isinstance(id, str):
         raise ValueError("O ID deve ser um numero inteiro")
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
      return num
    except ValueError as ve:
      print(f"Erro: {ve}. Por favor, tente novamente.") 

  def mostra_historico(self, tamanho, oceano):
    for linha in range(tamanho):
          if linha == 0:
              print(f'Y/X   {linha}', end='   ')
          else:
            print(f'{linha}', end='   ')
    print()
    for linha in range(tamanho):
          for coluna in range(tamanho):
              if coluna == 0:
                  print(f' {linha}   [{oceano[linha][coluna]}]', end=' ')
              else:
                  print(f'[{oceano[linha][coluna]}]', end=' ')
          print()

  def mostra_rank(self, rank):
    print(rank)
  
  def mostra_mensagem(self, msg):
    sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values
