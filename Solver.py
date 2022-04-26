# Implements BFS, DFS, GBFS and A* to solve n-by-n sliding puzzle

# goal state size 2
mapping2 = {
    # 2 1
    # 3
    0: {2, 1},
    1: {3, 0},
    2: {3, 0},
    3: {1, 2}
}


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
def breath_first_search(board):
    # TODO make dynamic
    # TODO remove print statements
    # TODO store necessary state for solution: path, depth, num_created, num_expanded, max_fringe
    queue = [board.list_as_str]
    print("The Queue below")
    print(queue)
    visited = set()
    visited.add(board.list_as_str)
    depth = 0
    while queue:
        size = len(queue)
        for i in range(size):
            current = queue.pop(0)
            # TODO might be able to increase expanded here because after queueing they are expanded
            print("current after pop")
            print(current)
            if current == '213 ':  # TODO this needs to be dynamic might just have a variable in class
                print("Goal State")
                print(current)
                return depth
            add_child(current, visited, queue)
        depth += 1
    return -1


# adds child to tree search TODO: verify if this function can be reused
def add_child(current: str, visited, queue):
    index = current.index(' ')
    for i in mapping2[index]:  # TODO make mapping dynamic
        print("i in add_child for loop before swap")
        print(i)
        s = swap(current, index, i)
        if s not in visited:
            print("visited")
            print(visited)
            queue.append(s)
            print("Queue")
            print(queue)
            visited.add(s)
            print("s that was appended and added")
            print(s)
        else:
            print("s was already visited")


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
