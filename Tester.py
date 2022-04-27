# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import sys
from Board import Board
from Solver import is_solvable, breath_first_search

# TODO: function to print to file


def prep_input(ter_input):
    output = [ter_input[1], ter_input[2], ter_input[3]]
    return output


def main():
    if len(sys.argv) == 4:
        args = prep_input(sys.argv)
        bfs2 = Board(int(args[0]), args[1], args[2])
        flag = is_solvable(bfs2)
        print(flag)
        bfs_test = breath_first_search(bfs2)
        print(bfs_test)

    else:
        print("Did not receive command line arguments")
        print("Running assignment requirements")
        # TODO have console display required output
        # TODO must also output to a readme.txt file
        size2 = 2
        size3 = 3
        size4 = 4

        init_state2 = "32 1"
        init_state3 = "47315862 "
        init_state4 = "123456789AB DEFC"

        bfs = "BFS"

        # running three sizes with bfs
        bfs2 = Board(size2, init_state2, bfs)
        breath_first_search(bfs2)
        print("depth bfs n = 2")
        print(bfs2.depth)
        print("expanded")
        print(bfs2.num_expanded)
        print("num created")
        print(bfs2.num_created)
        print("max fringe")
        print(bfs2.max_fringe)

        bfs3 = Board(size3, init_state3, bfs)
        breath_first_search(bfs3)
        print("depth bfs n = 3")
        print(bfs3.depth)
        print("expanded")
        print(bfs3.num_expanded)
        print("num created")
        print(bfs3.num_created)
        print("max fringe")
        print(bfs3.max_fringe)

        bfs4 = Board(size4, init_state4, bfs)
        breath_first_search(bfs4)
        print("depth bfs n = 4")
        print(bfs4.depth)
        print("expanded")
        print(bfs4.num_expanded)
        print("num created")
        print(bfs4.num_created)
        print("max fringe")
        print(bfs4.max_fringe)


main()
