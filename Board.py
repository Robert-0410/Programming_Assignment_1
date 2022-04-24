# Models an n-by-n board with sliding tiles.

# Class representing our state environment
class Board:

    def __init__(self, size, the_list, algorithm):
        self.size = size
        self.state = self.make_board(the_list)  # TODO: make 2D list
        self.algorithm = algorithm
        self.goal_state = ["", "", ""]  # TODO: this will contain the goal state once implemented

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


# Test function for testing code in this file
def test():
    t = Board(4, "123456789AB DEFC", "GBFS")
    print(t.state)
    # TODO: start on preliminary solvable


test()
