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
    print(inversions) # TODO: finish implementation

