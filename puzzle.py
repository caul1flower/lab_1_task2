"""
Module for the puzzle game.
GitHub: https://github.com/caul1flower/lab_1_task2.git
"""


def validate_board(board: list) -> bool:
    """
    Return if the board is ready for the game.

    >>> validate_board(board = ["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    return (
        horizontal_validation(board)
        and colomn_validation(board)
        and colour_validation(board)
    )


def horizontal_validation(board: list) -> bool:
    """
    Return if the horiontal requerments are satisfied.
    """
    board_set = set()
    board_lst = []
    for line in board:
        board_set |= set(line)
        board_lst.append(list(line))

    for elem in board_set:
        for line in board_lst:
            if line.count(elem) > 1 and elem != "*" and elem != " ":
                return False
    return True


def colomns(board: list) -> list:
    """
    Rerurn list of the colomns of the given board.
    """
    new_board = []
    for symbol in range(len(board)):
        new_line = []
        for line in board:
            new_line += line[symbol]
        new_line = "".join(new_line)
        new_board.append(new_line)
    return new_board


def colomn_validation(board: list) -> bool:
    """
    Return if the vertical requerments are satisfied.
    """
    new_board = colomns(board)
    return horizontal_validation(new_board)


def colour_validation(board: list) -> bool:
    """
    Return if the color requerments are satisfied.
    """
    row = -1
    vertical_board = colomns(board)
    new_board = []
    for elem in range(8):
        to_add = vertical_board[elem][: -elem - 1] + board[row][elem:]
        new_board.append(to_add)
        row -= 1
    return horizontal_validation(new_board)
