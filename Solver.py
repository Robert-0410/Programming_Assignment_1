# Implements BFS, DFS, GBFS and A* to solve n-by-n sliding puzzle
from Board import Board


class Node:

    # root node receives string 'root'
    def __init__(self, parent, state, board):
        self.parent = parent
        self.state = state
        self.algorithm = board.algorithm
        if self.algorithm == 'GBFS' or self.algorithm == 'A*':  # TODO only if the algorithm is greedy or A*
            self.size = board.size
            self.locations = self.get_goal_locations()
            self.heuristic = self.get_heuristics()

    # creates a list of states that represents the path found by the algorithm
    def get_path(self):
        current = self
        output = [current.state]
        while current.parent != 'root':
            current = current.parent
            output.insert(0, current.state)
        return output

    # returns heuristics value associated to the node based on Manhattan Distance
    def get_heuristics(self):
        curr_state = self.state
        zero_index = curr_state.index(' ')
        mod_state = curr_state[:zero_index] + '0' + curr_state[zero_index + 1:]
        output = 0
        for i in range(len(mod_state)):
            goal_row = self.locations[i].pop(0)
            goal_col = self.locations[i].pop(0)

            if i < 10:
                piece = str(i)
            else:
                piece = convert_digit_to_char(i)
            index = mod_state.index(piece)
            curr_row = int(index / self.size)
            curr_col = index % self.size
            output += abs(goal_row - curr_row) + abs(goal_col - curr_col)
        return output

    def get_goal_locations(self):
        size = len(self.state)
        if size == 4:
            return {
                # Goal state
                # 2 1
                # 3 0
                0: [1, 1],
                1: [0, 1],
                2: [0, 0],
                3: [1, 0]
            }
        elif size == 9:
            return {
                0: [0, 0],
                1: [0, 1],
                2: [0, 2],
                3: [1, 0],
                4: [1, 1],
                5: [1, 2],
                6: [2, 0],
                7: [2, 1],
                8: [2, 2]
            }
        elif size == 16:
            return {
                0: [3, 3],
                1: [0, 0],
                2: [0, 1],
                3: [0, 2],
                4: [0, 3],
                5: [1, 0],
                6: [1, 1],
                7: [1, 2],
                8: [1, 3],
                9: [2, 0],
                10: [2, 1],
                11: [2, 2],
                12: [2, 3],
                13: [3, 0],
                14: [3, 1],
                15: [3, 2]
            }
        else:
            print("Locations never got assigned in get_goal_locations()")


# Converts number to the corresponding character
def convert_digit_to_char(digit: int):
    output = ''
    if digit == 10:
        output = 'A'
    elif digit == 11:
        output = 'B'
    elif digit == 12:
        output = 'C'
    elif digit == 13:
        output = 'D'
    elif digit == 14:
        output = 'E'
    elif digit == 15:
        output = 'F'
    else:
        print("Digit did not get converted to char in convert_digit_to_char()")
    return output


# Counts number of inversions in a given list representation of an n x n game state
def inversion_count(the_list):
    output = 0
    blank_position = ' '
    for i in range(0, len(the_list)):
        for j in range(i + 1, len(the_list)):
            if the_list[j] != blank_position and the_list[i] != blank_position and the_list[i] > the_list[j]:
                output += 1
    return output


# determines if a game state is solvable
def is_solvable(board):
    inversions = inversion_count(board.the_list)

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


# Performs BFS on sliding puzzle for solution; fringe = queue
# returns -1 if failed, returns 0 if successful
def breath_first_search(board):
    visited = set()
    visited.add(board.list_as_str)
    root = Node("root", board.list_as_str, board)
    fringe = [root]
    depth = 0
    while fringe:
        size = len(fringe)
        if size > board.max_fringe:
            board.max_fringe = size
        for i in range(size):
            current = fringe.pop(0)
            board.num_expanded += 1
            if current.state == board.goal_state:
                board.path = current.get_path()
                return 0
            add_child(board, visited, current, fringe)

        depth += 1
        board.depth = depth
    return -1


# TODO: gets stuck after getting a solution found, will only get solution again if I change the mapping index 15
# Performs the given search algorithm (dfs) to an n x n sliding puzzle; fringe = stack
def depth_first_search(board):
    visited = set()
    visited.add(board.list_as_str)
    root = Node("root", board.list_as_str, board)
    fringe = [root]
    depth = 0
    while fringe:
        size = len(fringe)
        if size > board.max_fringe:
            board.max_fringe = size
        for i in range(size):
            current = fringe.pop()
            board.num_expanded += 1
            if current.state == board.goal_state:
                board.path = current.get_path()
                return 0
            add_child(board, visited, current, fringe)

        depth += 1
        board.depth = depth
    return -1


# Performs gbfs to an n x n sliding puzzle: fringe priority queue, f(x) = h(x)
# TODO implement
def greedy_best_first_search(board):
    return board  # temp


# Performs A* search to an n x n sliding puzzle; fringe priority queue, f(x) = g(x) + h(x)
# TODO implement
def a_star_search(board):
    return board  # temp


# TODO: implement: GBFS, A*

# adds child to tree search
def add_child(board, visited, current, fringe):
    index = current.state.index(' ')
    mapping = board.mapping
    for i in mapping[index]:
        s = swap(current.state, index, i)
        if s not in visited:
            visited.add(s)
            fringe.append(Node(current, s, board))
            board.num_created += 1


# conducts movement and returns updated state
def swap(current: str, index: int, i: int):
    s = list(current)
    s[index] = s[i]
    s[i] = ' '
    output = ''
    for i in s:
        output += i
    return output


# ----------------test code--------------------------
board2 = Board(2, "32 1", "A*")
test2 = Node("root", "32 1", board2)

board3 = Board(3, "15342678 ", "GBFS")
test3 = Node("root", board3.list_as_str, board3)

board4 = Board(4, "123456789AB DEFC", "A*")
test4 = Node("root", board4.list_as_str, board4)

print(test2.heuristic)
print(test3.heuristic)
print(test4.heuristic)
