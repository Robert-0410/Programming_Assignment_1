# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import sys
from Board import Board
from Solver import is_solvable, breath_first_search

# TODO: function to print to file
# TODO: redo user input with sys.argv


def prep_input(ter_input):
    output = [ter_input[1], ter_input[2], ter_input[3]]
    return output


def main():
    if len(sys.argv) == 4:
        args = prep_input(sys.argv)
        game = Board(int(args[0]), args[1], args[2])
        flag = is_solvable(game)
        print(flag)
        bfs_test = breath_first_search(game)
        print(bfs_test)

    else:
        print("Did not receive command line arguments")


main()
