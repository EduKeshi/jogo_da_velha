from jogo_da_velha import calculate_ia_move, enter_move, ia_move, make_board, make_list_of_free_fields, victory_for


# Teste do desenho do tabulerio
def test_faz_o_tabuleiro_3_por_3():
    tabuleiro = make_board()

    assert len(tabuleiro) == 3


def test_faz_o_tabuleiro_10_por_10():
    tabuleiro = make_board(10)


# Testando os movimentos
def test_faz_o_movimento_no_tabuleiro():
    status_do_tabuleiro = [
        ["0 0", "0 1", "0 2"],
        ["1 0", "1 1", "1 2"],
        ["2 0", "2 1", "2 2"]
    ]

    movimento = enter_move(status_do_tabuleiro, 0, 0)

    assert movimento[0][0] == "O"


# Teste dos campos vazios
def test_mostra_os_campos_vazios():
    status_do_tabuleiro = [
        ["O", "0 1", "0 2"],
        ["1 0", "1 1", "1 2"],
        ["2 0", "2 1", "2 2"]
    ]

    campos_livres = make_list_of_free_fields(status_do_tabuleiro)

    assert campos_livres == [("0", "1"), ("0", "2"), ("1", "0"), ("1", "1"), ("1", "2"), ("2", "0"), ("2", "1"), ("2", "2")]


def test_mostra_os_campos_vazios_2():
    status_do_tabuleiro = [
        ["O", "X", "0 2"],
        ["1 0", "O", "1 2"],
        ["X", "2 1", "X"]
    ]

    campos_livres = make_list_of_free_fields(status_do_tabuleiro)

    assert campos_livres == [("0", "2"), ("1", "0"), ("1", "2"), ("2", "1")]


# Teste das vitorias
def test_cenario_linha_1():
    board = [
        ["O", "O", "O"],
        ["1 0", "1 1", "1 2"],
        ["2 0", "2 1", "2 2"]
    ]

    vitoria = victory_for(board, "O")

    assert vitoria is True


def test_cenario_linha_2():
    board = [
        ["0 0", "0 1", "0 2"],
        ["O", "O", "O"],
        ["2 0", "2 1", "2 2"]
    ]

    vitoria = victory_for(board, "O")

    assert vitoria is True


def test_cenario_linha_3():
    board = [
        ["0 0", "0 1", "0 2"],
        ["1 0", "1 1", "1 2"],
        ["O", "O", "O"]
    ]

    vitoria = victory_for(board, "O")

    assert vitoria is True


def test_coluna_1():
    board = [
        ["O", "0 1", "0 2"],
        ["O", "1 1", "1 2"],
        ["O", "2 1", "2 2"]
    ]

    vitoria = victory_for(board, "O")

    assert vitoria is True


def test_coluna_2():
    board = [
        ["0 0", "O", "0 2"],
        ["1 0", "O", "1 2"],
        ["2 0", "O", "2 2"]
    ]

    vitoria = victory_for(board, "O")

    assert vitoria is True


def test_coluna_3():
    board = [
        ["0 0", "0 1", "O"],
        ["1 0", "1 1", "O"],
        ["2 0", "2 1", "O"]
    ]

    vitoria = victory_for(board, "O")

    assert vitoria is True


def test_tranversal():
    board = [
        ["O", "0 1", "0 2"],
        ["1 0", "O", "1 2"],
        ["2 0", "2 1", "O"]
    ]

    vitoria = victory_for(board, "O")

    assert vitoria is True


def test_transversal_inversa():
    board = [
        ["0 0", "0 1", "O"],
        ["1 0", "O", "1 2"],
        ["O", "2 1", "2 2"]
    ]

    vitoria = victory_for(board, "O")

    assert vitoria is True


def test_cenario_linha_1_x():
    board = [
        ["X", "X", "X"],
        ["1 0", "1 1", "1 2"],
        ["2 0", "2 1", "2 2"]
    ]

    vitoria = victory_for(board, "X")

    assert vitoria is True


def test_cenario_linha_2_x():
    board = [
        ["0 0", "0 1", "0 2"],
        ["X", "X", "X"],
        ["2 0", "2 1", "2 2"]
    ]

    vitoria = victory_for(board, "X")

    assert vitoria is True


def test_cenario_linha_3_x():
    board = [
        ["0 0", "0 1", "0 2"],
        ["1 0", "1 1", "1 2"],
        ["X", "X", "X"]
    ]

    vitoria = victory_for(board, "X")

    assert vitoria is True


def test_coluna_1_x():
    board = [
        ["X", "0 1", "0 2"],
        ["X", "1 1", "1 2"],
        ["X", "2 1", "2 2"]
    ]

    vitoria = victory_for(board, "X")

    assert vitoria is True


def test_coluna_2_x():
    board = [
        ["0 0", "X", "0 2"],
        ["1 0", "X", "1 2"],
        ["2 0", "X", "2 2"]
    ]

    vitoria = victory_for(board, "X")

    assert vitoria is True


def test_coluna_3_x():
    board = [
        ["0 0", "0 1", "X"],
        ["1 0", "1 1", "X"],
        ["2 0", "2 1", "X"]
    ]

    vitoria = victory_for(board, "X")

    assert vitoria is True


def test_tranversal_x():
    board = [
        ["X", "0 1", "0 2"],
        ["1 0", "X", "1 2"],
        ["2 0", "2 1", "X"]
    ]

    vitoria = victory_for(board, "X")

    assert vitoria is True


def test_transversal_inversa_x():
    board = [
        ["0 0", "0 1", "X"],
        ["1 0", "X", "1 2"],
        ["X", "2 1", "2 2"]
    ]

    vitoria = victory_for(board, "X")

    assert vitoria is True


def test_velha():
    board = [
        ["O", "O", "X"],
        ["X", "X", "O"],
        ["O", "X", "O"]
    ]

    vitoria = victory_for(board, "O")

    assert vitoria is True


# Teste do movimento da máquina
def test_coloca_um_x_no_tabuleiro():
    board = [
        ["0 0", "0 1", "0 2"],
        ["1 0", "1 1", "1 2"],
        ["2 0", "2 1", "2 2"]
    ]

    movimentos = ia_move(board, 0, 1)

    assert "X" in movimentos[0][1]


# Teste dos numeros da jogada
def test_retorna_numeros_que_nao_estao_ocupados():

    board = [
        ["O", "X", "O"],
        ["1 0", "X", "O"],
        ["X", "O", "X"]
    ]
    jogada_da_linha, jogada_da_coluna = calculate_ia_move(board)

    assert jogada_da_linha == 1 and jogada_da_coluna == 0


def test_nao_pode_retornar_numeros_que_estao_ocupados():
    board = [
        ["O", "0 1", "0 2"],
        ["1 0", "1 1", "1 2"],
        ["2 0", "2 1", "2 2"]
    ]

    jogada_da_linha, jogada_da_coluna = calculate_ia_move(board)

    jogada = (jogada_da_linha, jogada_da_coluna)

    assert jogada != (0, 0)
