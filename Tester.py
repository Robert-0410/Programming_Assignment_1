# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# TODO: redo user input with sys.argv
import sys
# TODO: function to print to file


def prep_input(ter_input):
    output = [ter_input[1], ter_input[2], ter_input[3]]
    return output


def main():
    args = prep_input(sys.argv)
    for i in args:
        print(i)


main()
