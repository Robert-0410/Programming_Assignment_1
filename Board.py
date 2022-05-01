# Models an n-by-n board with sliding tiles.


# Game board for size 2 x 2
mapping2 = {
    # 2 1
    # 3
    0: {1, 2},
    1: {0, 3},
    2: {0, 3},
    3: {1, 2}
}

# Game board for size 3 x 3
mapping3 = {
    # 0 1 2
    # 3 4 5
    # 6 7 8
    0: {1, 3},
    1: {0, 2, 4},
    2: {1, 5},
    3: {0, 4, 6},
    4: {1, 3, 5, 7},
    5: {2, 4, 8},
    6: {3, 7},
    7: {4, 6, 8},
    8: {5, 7}
}

# Game board for size 4 x 4
mapping4 = {
    # 0  1  2  3
    # 4  5  6  7
    # 8  9  10 11
    # 12 13 14 15
    0: {1, 4},
    1: {0, 2, 5},
    2: {1, 3, 6},
    3: {2, 7},
    4: {0, 5, 8},
    5: {1, 4, 6, 9},
    6: {2, 5, 7, 10},
    7: {3, 6, 11},
    8: {4, 9, 12},
    9: {5, 8, 10, 13},
    10: {6, 9, 11, 14},
    11: {15, 7, 10},  # messing with index = 11, since it is the first blank spot
    12: {8, 13},
    13: {9, 12, 14},
    14: {10, 13, 15},
    15: {11, 14}
}

# goal states for size 2, 3, and 4
goal2 = "213 "
goal3 = " 12345678"
goal4 = "123456789ABCDEF "


# mapping assignment
def set_mapping(size: int):
    if size == 2:
        return mapping2
    elif size == 3:
        return mapping3
    elif size == 4:
        return mapping4
    else:
        print("Error: mapping was never assigned in set_mapping()")


# goal state assignment
def set_goal_state(size: int):
    if size == 2:
        return goal2
    elif size == 3:
        return goal3
    elif size == 4:
        return goal4
    else:
        print("Error: goal state was never assigned in set_goal_state()")


# Class representing our state environment
class Board:

    # constructor
    def __init__(self, size, the_list, algorithm):
        self.the_list = [char for char in the_list]
        self.list_as_str = the_list
        self.size = size
        self.state = self.make_board(the_list)
        self.row_of_blank = find_blank_spot(size, the_list)
        self.algorithm = algorithm
        self.goal_state = set_goal_state(size)
        self.mapping = set_mapping(size)

        # state for assignment requirements
        self.path = [""]
        self.depth = 0
        self.num_created = 0
        self.num_expanded = 0
        self.max_fringe = 0

    # makes the state into a 2D list
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


# identifies the location of the blank location
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
