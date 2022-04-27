# Implements BFS, DFS, GBFS and A* to solve n-by-n sliding puzzle


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


# Performs BFS on sliding puzzle for solution
# returns -1 if failed, returns 0 if successful
def breath_first_search(board):
    # TODO store necessary state for solution: path
    # TODO for finding the path try try paralleling the data structures but with nodes instead
    queue = [board.list_as_str]
    visited = set()
    visited.add(board.list_as_str)
    depth = 0
    while queue:
        size = len(queue)
        if size > board.max_fringe:
            board.max_fringe = size
        for i in range(size):
            current = queue.pop(0)
            board.num_expanded += 1
            if current == board.goal_state:
                # TODO once goal state is found we can back track to identify path
                return 0
            add_child(board, current, visited, queue)
        depth += 1
        board.depth = depth
    return -1


# adds child to tree search TODO: verify if this function can be reused
def add_child(board, current: str, visited, queue):
    index = current.index(' ')
    mapping = board.mapping
    for i in mapping[index]:
        s = swap(current, index, i)
        if s not in visited:
            queue.append(s)
            visited.add(s)
            board.num_created += 1


# conducts movement and returns updated state TODO verify if function can be reused in other algos
def swap(current: str, index: int, i: int):
    s = list(current)
    s[index] = s[i]
    s[i] = ' '
    output = ''
    for i in s:
        output += i
    return output

# TODO: implement: BFS, DFS, GBFS, A*
