# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import sys
from Board import Board
from Solver import is_solvable, breath_first_search, depth_first_search, greedy_best_first_search, a_star_search


# TODO: function to print to file


def prep_input(ter_input):
    output = [ter_input[1], ter_input[2], ter_input[3]]
    return output


def main():
    if len(sys.argv) == 4:
        # TODO adjust logic to run specified algorithm by command line arguments
        args = prep_input(sys.argv)
        num_2 = Board(int(args[0]), args[1], args[2])
        flag = is_solvable(num_2)
        print(flag)
        bfs_test = breath_first_search(num_2)
        print(bfs_test)
        # TODO have console display required output
        # TODO must also output to a readme.txt file

    else:
        print("Did not receive command line arguments")
        print("Running with assignment requirements")
        # TODO have console display required output
        # TODO must also output to a readme.txt file
        size2 = 2
        size3 = 3
        size4 = 4

        init_state2 = "32 1"
        init_state3 = "47315862 "
        init_state4 = "123456789AB DEFC"

        bfs = "BFS"
        dfs = "DFS"
        gbfs = "GBFS"
        a_star = "A*"

        # running three sizes with bfs
        num_2 = Board(size2, init_state2, a_star)
        #  breath_first_search(num_2)
        a_star_search(num_2)
        print("depth bfs n = 2")
        print(num_2.depth)
        print("expanded")
        print(num_2.num_expanded)
        print("num created")
        print(num_2.num_created)
        print("max fringe")
        print(num_2.max_fringe)
        print("Path is:")
        print(num_2.path)
        print("---------------------------------------------------------------num_2 done")

        num_3 = Board(size3, init_state3, a_star)
        #  breath_first_search(num_3)
        a_star_search(num_3)
        print("depth bfs n = 3")
        print(num_3.depth)
        print("expanded")
        print(num_3.num_expanded)
        print("num created")
        print(num_3.num_created)
        print("max fringe")
        print(num_3.max_fringe)
        print("Path is:")
        print(num_3.path)
        print("-----------------------------------------------------------------num_3 done")

        num_4 = Board(size4, init_state4, a_star)
        #  breath_first_search(num_4)
        a_star_search(num_4)
        print("depth bfs n = 4")
        print(num_4.depth)
        print("expanded")
        print(num_4.num_expanded)
        print("num created")
        print(num_4.num_created)
        print("max fringe")
        print(num_4.max_fringe)
        print("Path is:")
        print(num_4.path)


main()
