import PySimpleGUI as sg

class TelaJogador():
  def __init__(self):
     self.__window = None
     self.init_opcoes()

  def tela_opcoes(self):
    self.init_opcoes()
    button, values = self.__window.Read()
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
      [sg.Text('---------- Tela Jogador ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Incluir Jogador', "RD1", key='1')],
      [sg.Radio('Alterar Jogador', "RD1", key='2')],
      [sg.Radio('Listar Jogadores', "RD1", key='3')],
      [sg.Radio('Mostrar Histórico', "RD1", key='4')],
      [sg.Radio('Mostrar Ranking dos Jogadores', "RD1", key='5')],
      [sg.Radio('Seção de Partida', "RD1", key='6')],
      [sg.Radio('Excluir Jogador', "RD1", key='7')],
      [sg.Radio('Retornar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de Jogadores').Layout(layout)
  
  def dados_jogador(self):
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- DADOS JOGADOR ----------', font=("Helvica", 25))],
      [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
      [sg.Text('Data Nascimento:', size=(15, 1)), sg.InputText('', key='data_nascimento')],
      [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de Cadastro').Layout(layout)

    button, values = self.open()
    nome = values['nome']
    data_nascimento = values['data_nascimento']
    id = int(values['id'])

    self.close()
    return {"nome": nome, "data_nascimento": data_nascimento, "id": id}

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
    string_todos_jogadores = ""
    for dado in dados_jogador:
      string_todos_jogadores = string_todos_jogadores + "NOME: " + dado["nome"] + '\n'
      string_todos_jogadores = string_todos_jogadores + "NASCIMENTO DO JOGADOR: " + str(dado["data_nascimento"]) + '\n'
      string_todos_jogadores = string_todos_jogadores + "ID DO JOGADOR: " + str(dado["id"]) + '\n\n'

    sg.Popup('-------- LISTA DE JOGADORES ----------', string_todos_jogadores)

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

  def mostra_rank(self, rank_info):
    layout = [
            [sg.Text('---- RANK ----', font=("Helvica", 25))],
            *[[sg.Text(f'{pos}º - {nome} Pontuação: {pontuacao}')] for pos, nome, pontuacao in rank_info],
            [sg.Button('OK')]
        ]
    window = sg.Window('Ranking', layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'OK'):
            break
    
    window.close()
  
  def mostra_mensagem(self, msg):
    sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values
