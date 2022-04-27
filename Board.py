# Models an n-by-n board with sliding tiles.


# Class representing our state environment
from Solver import is_solvable

# Game board for size 2 x 2
mapping2 = {
    # 2 1
    # 3
    0: {2, 1},
    1: {3, 0},
    2: {3, 0},
    3: {1, 2}
}

# Game board for size 3 x 3
# TODO fix mapping
mapping3 = {
    # 0 1 2
    # 3 4 5
    # 6 7 8
    0: {2, 1},
    1: {3, 0},
    2: {3, 0},
    3: {1, 2},
    4: {},
    5: {},
    6: {},
    7: {},
    8: {}
}

# Game board for size 4 x 4
# TODO fix mappingi
mapping4 = {
    # 2 1
    # 3
    0: {2, 1},
    1: {3, 0},
    2: {3, 0},
    3: {1, 2},
    4: {},
    5: {},
    6: {},
    7: {},
    8: {},
    9: {},
    10: {},
    11: {},
    12: {},
    13: {},
    14: {},
    15: {}
}


# TODO: might have to create my own state class or node
class Board:

    def __init__(self, size, the_list, algorithm):
        self.the_list = [char for char in the_list]
        self.list_as_str = the_list
        self.size = size
        self.state = self.make_board(the_list)
        self.row_of_blank = find_blank_spot(size, the_list)
        self.algorithm = algorithm
        self.goal_state = [""]  # TODO: this will contain the goal state once implemented
        self.path = [""]  # TODO: will contain solution path once implemented
        self.depth = 0  # TODO: depth of solution once implemented
        self.num_created = 0  # TODO: counter for nodes of the search tree that are created
        self.num_expanded = 0  # TODO: nodes that have been expanded
        self.max_fringe = 0  # TODO: max size of fringe at any point during the search

    def make_board(self, the_list):
        end = self.size
        current = 0
        temp = [""]
        output = temp * self.size
        for i in range(end):
            row = [""] * self.size

            for j in range(end):
                row[j] = the_list[current]
                current = current + 1

            output[i] = row

        return output


def find_blank_spot(size, the_list):
    index = the_list.find(' ')
    helper = size
    row = 0

    for i in range(0, (size * size)):
        if index < helper:
            break
        elif index >= helper:
            row = row + 1
            helper = helper + size

    return row


# Test function for testing code in this file
def test():
    t = Board(4, "123456789AB DEFC", "GBFS")
    print(t.state)
    print(t.the_list)
    flag = is_solvable(t)
    print(t.row_of_blank)
    print(flag)

# test()
