# Implements BFS, DFS, GBFS and A* to solve n-by-n sliding puzzle

# goal state size 2
mapping2 = {
    # 2 1
    # 3
    0: {'1', '3'},
    1: {'2', ' '},
    2: {'2', ' '},
    3: {'1', '1'}
}


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
def breath_first_search(board):
    # TODO needs to be fixed along with helper functions
    queue = [board.state]
    print(queue)
    visited = set(board.state)
    depth = 0
    while queue:
        size = len(queue)
        for i in range(size):
            current = queue.pop(0)
            if current == '213 ':
                return depth
            add_child(current, visited, queue)
        depth += 1
    return -1


def add_child(current: str, visited, queue):
    index = current.index(' ')
    for i in mapping2[index]:
        s = swap(current, index, i)
        if s not in visited:
            queue.append(s)
            visited.add(s)


def swap(current: str, index, i):
    s = list(current)
    s[index] = s[i]
    s[i] = ' '
    ss = ''
    for i in s:
        ss += i
    return ss

# TODO: implement: BFS, DFS, GBFS, A*
