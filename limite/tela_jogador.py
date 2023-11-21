import PySimpleGUI as sg

class TelaJogador():
  def __init__(self):
     self.__window = None

  def tela_opcoes(self):
    self.init_opcoes()
    while True:
      event, values = self.__window.read()

      if event == sg.WIN_CLOSED or event == 'Cancelar':
        opcao = 0
        break
      elif any(values.values()):
        opcao = next((int(key) for key, value in values.items() if value), None)
        break

    self.close()
    return opcao

  def init_opcoes(self):
    sg.ChangeLookAndFeel('LightBlue')
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
    layout = [
        [sg.Text('-------- DADOS JOGADOR ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('Data Nascimento:', size=(15, 1)), sg.CalendarButton('Escolher Data', target='data_nascimento', format='%d/%m/%Y', key='data_nascimento')],
        [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    window = sg.Window('Sistema de Cadastro', layout)

    while True:
        event, values = window.Read()

        if event in (None, 'Cancelar'):
            window.close()
            return None

        if event == 'Confirmar':
            try:
                nome = values['nome']
                data_nascimento = values['data_nascimento']
                jogador_id = values['id']

                if not nome or not data_nascimento or jogador_id == "":
                    raise ValueError("Todos os campos devem ser preenchidos.")

                try:
                    jogador_id = int(jogador_id)
                except ValueError:
                    raise ValueError("O ID deve ser um número inteiro.")

                sg.popup(f"Informações do Jogador: Nome={nome}, Data Nascimento={data_nascimento}, ID={jogador_id}")
                window.close()
                return {"nome": nome, "data_nascimento": data_nascimento, "id": jogador_id}

            except ValueError as ve:
                sg.popup_error(f"Erro: {ve}")

    window.close()

  def seleciona_jogador(self, lista_jogadores):
    if not lista_jogadores:
      sg.popup("Não há jogadores disponíveis. Adicione jogadores antes de prosseguir.")
      return None

    jogadores = [(jogador.id, jogador.nome) for jogador in lista_jogadores]

    layout = [
        [sg.Text('Selecione um jogador:')],
        [sg.Listbox(values=jogadores, size=(30, 6), key='jogadores')],
        [sg.Button('OK')]
    ]

    window = sg.Window('Selecionar Jogador', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            return None

        try:
            jogador_selecionado = values['jogadores'][0]
            jogador_id = int(jogador_selecionado[0])
            window.close()
            return jogador_id

        except (IndexError, ValueError):
            sg.popup_error("Por favor, selecione um jogador.")

    window.close()

  def mostra_jogador(self, dados_jogador):
    layout = [
            [sg.Text('-------- LISTA DE JOGADORES ----------')],
            *[
                [sg.Text(f"NOME: {dado['nome']}"), sg.Text(f"NASCIMENTO DO JOGADOR: {dado['data_nascimento']}"),
                 sg.Text(f"ID DO JOGADOR: {dado['id']}")] for dado in dados_jogador
            ],
            [sg.Button('OK')]
        ]

    window = sg.Window('Lista de Jogadores', layout)

    while True:
      event, values = window.read()

      if event == sg.WIN_CLOSED or event == 'OK':
        break

    window.close()

  def seleciona_partida(self, partidas):
    layout = [
            [sg.Text('Selecione uma partida:')],
            [sg.Listbox(values=partidas, size=(30, 5), key='PARTIDAS')],
            [sg.Button('OK')]
        ]

    window = sg.Window('Selecionar Partida', layout)

    while True:
      event, values = window.read()

      if event == sg.WIN_CLOSED or event == 'OK':
        selected_index = values['PARTIDAS'][0] if values['PARTIDAS'] else None
        window.close()
        return selected_index

    window.close()

  def mostra_historico(self, tamanho, oceano):
    layout = [
            [sg.Text('---Histórico do Oceano---')]
        ]

    for linha in range(tamanho):
      linha_layout = []
      for coluna in range(tamanho):
        linha_layout.append(sg.Text(f'[{oceano[linha][coluna]}]', size=(5, 1), key=f'pos_{linha}_{coluna}'))
      layout.append(linha_layout)

    window = sg.Window('Histórico', layout)

    while True:
      event, values = window.read()

      if event == sg.WIN_CLOSED:
        break

    window.close()

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
