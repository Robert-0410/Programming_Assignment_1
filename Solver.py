# Implements BFS, DFS, GBFS and A* to solve n-by-n sliding puzzle


class Node:

    # root node receives string 'root'
    def __init__(self, parent, state):
        self.parent = parent
        self.state = state
        # TODO assign each node a heuristic

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
        return self


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
    root = Node("root", board.list_as_str)
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
    root = Node("root", board.list_as_str)
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
            fringe.append(Node(current, s))
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

initial_state = '32 1'
initial_state3 = '15342678 '
size_test = 2

locations2 = {
    # Goal state
    # 2 1
    # 3 0
    0: [1, 1],
    1: [0, 1],
    2: [0, 0],
    3: [1, 0]
}

locations3 = {
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


def calculateManhattan(initial_state):
    # TODO argument must be a Node , and board.goal_state
    input_str = initial_state  # TODO change to node state
    zero_index = input_str.index(' ')
    mod_state = input_str[:zero_index] + '0' + input_str[zero_index + 1:]

    output = 0
    for i in range(len(mod_state)):
        goal_row = locations2[i].pop(0)
        goal_col = locations2[i].pop(0)  # TODO make locations dynamic

        piece = str(i)
        index = mod_state.index(piece)
        curr_row = int(index / size_test)
        curr_col = index % size_test
        output += abs(goal_row - curr_row) + abs(goal_col - curr_col)
    return output

# print(calculateManhattan(initial_state))
# print(locations2[1].pop(0))
# print(locations2)
# print(locations2[1].pop(0))
# print(locations2)
