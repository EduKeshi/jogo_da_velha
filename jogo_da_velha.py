from random import randrange


class LugarInvalidoError(Exception):
    pass


def make_board(size=3):
    # The function accepts one parameter containing the board's current status
    board = [[f"{linhas} {colunas}" for colunas in range(size)] for linhas in range(size)]

    return board


def display_board(board: list):
    print("\nTabuleiro do jogo:\n")
    for linha in board:
        print(linha)  # and prints it out to the console.


def ask_move():
    colocou_valores_errados = True
    while colocou_valores_errados:
        # The function accepts the board's current status, asks the user about their move,
        try:
            linha_da_jogada = int(input("\nQual linha você vai querer jogar?: "))
            coluna_da_jogada = int(input("\nQual coluna você vai querer jogar?: "))
            colocou_valores_errados = False
        except ValueError:
            print("\n~Só é permitido colocar números\nJogue novamente~\n")

    return linha_da_jogada, coluna_da_jogada


def enter_move(status_do_tabuleiro: list, linha_da_jogada: int, coluna_da_jogada: int):
    jogou_no_lugar_errado = True
    while jogou_no_lugar_errado:
        try:
            # checks the input, and updates the board according to the user's decision.
            validacao_do_x = "X" not in status_do_tabuleiro[linha_da_jogada][coluna_da_jogada]
            validacao_do_o = "O" not in status_do_tabuleiro[linha_da_jogada][coluna_da_jogada]
            if not validacao_do_x or not validacao_do_o:
                raise LugarInvalidoError()
            status_do_tabuleiro[linha_da_jogada][coluna_da_jogada] = "O"
            jogou_no_lugar_errado = False
        except IndexError:
            print("\n~Para as linhas e colunas só pode usar valores de 0 a 2\nJogue novamente~\n")
        except LugarInvalidoError:
            print("\n~Lugar já ocupado, escolha outro lugar para jogar~\n")
            linha_da_jogada, coluna_da_jogada = ask_move()

    return status_do_tabuleiro


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    lugares_livres = []
    for tabuleiro in board:
        for lugar in tabuleiro:
            if lugar == "X" or lugar == "O":
                continue
            lugares_livres.append((lugar[0], lugar[2]))

    return lugares_livres


def victory_for(board: list, sign: str):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    vitoria_em_linha_reta = sign in board[0][0] and sign in board[0][1] and sign in board[0][2] or \
                            sign in board[1][0] and sign in board[1][1] and sign in board[1][2] or \
                            sign in board[2][0] and sign in board[2][1] and sign in board[2][2]

    vitoria_de_cima_para_baixo = sign in board[0][0] and sign in board[1][0] and sign in board[2][0] or \
                                 sign in board[0][1] and sign in board[1][1] and sign in board[2][1] or \
                                 sign in board[0][2] and sign in board[1][2] and sign in board[2][2]

    vitoria_na_transversal = sign in board[0][0] and sign in board[1][1] and sign in board[2][2] or \
                             sign in board[0][2] and sign in board[1][1] and sign in board[2][0]

    velha = len(make_list_of_free_fields(board)) == 0

    if vitoria_em_linha_reta or vitoria_de_cima_para_baixo or vitoria_na_transversal:
        if sign == "O":
            print("Parabéns, você venceu o jogo!")
        else:
            print("Eu ganhei o jogo, vamos de novo?")
        return True
    if velha:
        print("Deu velha, vamos de novo?")
        return True

    return False


def calculate_ia_move(board):
    # The function draws the computer's move and updates the board.
    nao_jogou_em_um_lugar_vazio = True

    while nao_jogou_em_um_lugar_vazio:
        jogada_da_linha = randrange(0, 3)
        jogada_da_coluna = randrange(0, 3)
        if board[jogada_da_linha][jogada_da_coluna] != "O" and \
                board[jogada_da_linha][jogada_da_coluna] != "X":
            nao_jogou_em_um_lugar_vazio = False

    return jogada_da_linha, jogada_da_coluna


def ia_move(board: list, jogada_da_linha: int, jogada_da_coluna: int):
    board[jogada_da_linha][jogada_da_coluna] = "X"

    return board


if __name__ == "__main__":
    # Montagem do tabuleiro
    status_do_tabuleiro = make_board()
    display_board(status_do_tabuleiro)
    verificar_se_alguem_ganhou = False

    while not verificar_se_alguem_ganhou:
        # As jogadas no tabuleiro
        linha, coluna = ask_move()
        status_do_tabuleiro = enter_move(status_do_tabuleiro, linha, coluna)
        display_board(status_do_tabuleiro)

        # Verificação se alguém ganhou
        verificar_se_alguem_ganhou = victory_for(status_do_tabuleiro, "O")
        if verificar_se_alguem_ganhou:
            break

        # Minha jogada
        jogada_da_linha, jogada_da_coluna = calculate_ia_move(status_do_tabuleiro)
        status_do_tabuleiro = ia_move(status_do_tabuleiro, jogada_da_linha, jogada_da_coluna)
        display_board(status_do_tabuleiro)

        # Verificação se alguém ganhou
        verificar_se_alguem_ganhou = victory_for(status_do_tabuleiro, "X")
        if verificar_se_alguem_ganhou:
            break

        # Lugares livres
        lugares_livres = make_list_of_free_fields(status_do_tabuleiro)
        print(f"\nLugares livres {lugares_livres}\n")
