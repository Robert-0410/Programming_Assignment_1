import sys
from Board import Board
from Solver import breath_first_search, depth_first_search, greedy_best_first_search, a_star_search


def prep_input(ter_input):
    output = [ter_input[1], ter_input[2], ter_input[3]]
    return output


def main():
    if len(sys.argv) == 4:
        # TODO adjust logic to run specified algorithm by command line arguments
        args = prep_input(sys.argv)
        board = Board(int(args[0]), args[1], args[2])
        if args[2] == "BFS":
            breath_first_search(board)
        elif args[2] == "DFS":
            depth_first_search(board)
        elif args[2] == "GBFS":
            greedy_best_first_search(board)
        elif args[2] == "A*":
            a_star_search(board)
        else:
            print("Algorithm not supported")
        # TODO have console display required output
        print("Size: 2")
        print(args[2])
        print(board.path)
        # TODO must also output to a readme.txt file

        with open('Readme.txt', 'w') as file:
            file.writelines(
                ["Size: ", str(board.size), "\nInitial State: ", board.list_as_str, "\nGoal State: ", board.goal_state])
            file.writelines(["\n", board.algorithm, ": ", str(board.depth), ", ", str(board.num_created), ", ",
                             str(board.num_expanded), ", ", str(board.max_fringe)])

    else:
        print("Did not receive command line arguments")
        print("Running with assignment requirements")
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

        # n = 2
        bfs_2 = Board(size2, init_state2, bfs)
        dfs_2 = Board(size2, init_state2, dfs)
        gbfs_2 = Board(size2, init_state2, gbfs)
        a_star_2 = Board(size2, init_state2, a_star)

        breath_first_search(bfs_2)
        depth_first_search(dfs_2)
        greedy_best_first_search(gbfs_2)
        a_star_search(a_star_2)

        # n = 3
        bfs_3 = Board(size3, init_state3, bfs)
        dfs_3 = Board(size3, init_state3, dfs)
        gbfs_3 = Board(size3, init_state3, gbfs)
        a_star_3 = Board(size3, init_state3, a_star)

        breath_first_search(bfs_3)
        depth_first_search(dfs_3)
        greedy_best_first_search(gbfs_3)
        a_star_search(a_star_3)

        # n = 4
        bfs_4 = Board(size4, init_state4, bfs)
        dfs_4 = Board(size4, init_state4, dfs)
        gbfs_4 = Board(size4, init_state4, gbfs)
        a_star_4 = Board(size4, init_state4, a_star)

        breath_first_search(bfs_4)
        depth_first_search(dfs_4)
        greedy_best_first_search(gbfs_4)
        a_star_search(a_star_4)

        print("Size: 2")
        print("Breath First Search")
        print(bfs_2.path)
        print("Depth First Search")
        print(dfs_2.path)
        print("Greedy Best First Search")
        print(gbfs_2.path)
        print("A* Search")
        print(a_star_2.path)

        print("----------------------------------------")
        print("Size: 3")
        print("Breath First Search")
        print(bfs_3.path)
        print("Depth First Search")
        print(dfs_3.path)
        print("Greedy Best First Search")
        print(gbfs_3.path)
        print("A* Search")
        print(a_star_3.path)

        print("----------------------------------------")
        print("Size: 4")
        print("Breath First Search")
        print(bfs_4.path)
        print("Depth First Search")
        print(dfs_4.path)
        print("Greedy Best First Search")
        print(gbfs_4.path)
        print("A* Search")
        print(a_star_4.path)

        with open('Readme.txt', 'w') as file:
            file.writelines(
                ["Size: ", str(size2), "\nInitial State: ", init_state2, "\nGoal State: ", bfs_2.goal_state])
            file.writelines(["\n", bfs_2.algorithm, ": ", str(bfs_2.depth), ", ", str(bfs_2.num_created), ", ",
                             str(bfs_2.num_expanded), ", ", str(bfs_2.max_fringe)])
            file.writelines(["\n", dfs_2.algorithm, ": ", str(dfs_2.depth), ", ", str(dfs_2.num_created), ", ",
                             str(dfs_2.num_expanded), ", ", str(dfs_2.max_fringe)])
            file.writelines(["\n", gbfs_2.algorithm, ": ", str(gbfs_2.depth), ", ", str(gbfs_2.num_created), ", ",
                             str(gbfs_2.num_expanded), ", ", str(gbfs_2.max_fringe)])
            file.writelines(["\n", a_star_2.algorithm, ": ", str(a_star_2.depth), ", ", str(a_star_2.num_created), ", ",
                             str(a_star_2.num_expanded), ", ", str(a_star_2.max_fringe), "\n\n"])

            file.writelines(
                ["Size: ", str(size3), "\nInitial State: ", init_state3, "\nGoal State: ", bfs_3.goal_state])
            file.writelines(["\n", bfs_3.algorithm, ": ", str(bfs_3.depth), ", ", str(bfs_3.num_created), ", ",
                             str(bfs_3.num_expanded), ", ", str(bfs_3.max_fringe)])
            file.writelines(["\n", dfs_3.algorithm, ": ", str(dfs_3.depth), ", ", str(dfs_3.num_created), ", ",
                             str(dfs_3.num_expanded), ", ", str(dfs_3.max_fringe)])
            file.writelines(["\n", gbfs_3.algorithm, ": ", str(gbfs_3.depth), ", ", str(gbfs_3.num_created), ", ",
                             str(gbfs_3.num_expanded), ", ", str(gbfs_3.max_fringe)])
            file.writelines(["\n", a_star_3.algorithm, ": ", str(a_star_3.depth), ", ", str(a_star_3.num_created), ", ",
                             str(a_star_3.num_expanded), ", ", str(a_star_3.max_fringe), "\n\n"])

            file.writelines(
                ["Size: ", str(size4), "\nInitial State: ", init_state4, "\nGoal State: ", bfs_4.goal_state])
            file.writelines(["\n", bfs_4.algorithm, ": ", str(bfs_4.depth), ", ", str(bfs_4.num_created), ", ",
                             str(bfs_4.num_expanded), ", ", str(bfs_4.max_fringe)])
            file.writelines(["\n", dfs_4.algorithm, ": ", str(dfs_4.depth), ", ", str(dfs_4.num_created), ", ",
                             str(dfs_4.num_expanded), ", ", str(dfs_4.max_fringe)])
            file.writelines(["\n", gbfs_4.algorithm, ": ", str(gbfs_4.depth), ", ", str(gbfs_4.num_created), ", ",
                             str(gbfs_4.num_expanded), ", ", str(gbfs_4.max_fringe)])
            file.writelines(["\n", a_star_4.algorithm, ": ", str(a_star_4.depth), ", ", str(a_star_4.num_created), ", ",
                             str(a_star_4.num_expanded), ", ", str(a_star_4.max_fringe), "\n\n"])
            file.close()


main()
