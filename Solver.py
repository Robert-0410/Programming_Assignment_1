# Implements BFS, DFS, GBFS and A* to solve n-by-n sliding puzzle
def inversion_count(the_list, size):
    output = 0
    blank_position = ' '
    for i in range(0, len(the_list)):
        for j in range(i + 1, len(the_list)):
            if the_list[j] != blank_position and the_list[i] != blank_position and the_list[i] > the_list[j]:
                output += 1
    return output


def is_solvable(board):
    inversions = inversion_count(board.the_list, board.size)

    output = True
    # odd case for board size
    if board.size % 2 == 1 and inversions % 2 == 1:
        output = False
    # even case
    elif board.size % 2 == 0:
        check = inversions + board.row_of_blank
        if check % 2 == 1:
            output = True
        else:
            output = False

    return output


# TODO: implement: BFS, DFS, GBFS, A*

