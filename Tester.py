# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
print("Input in the form: [size] \"[initialstate]\" [searchmethod] example: 2 \"32 1\" DFS")
userInput = input("Enter input: ")

tokens = userInput.split()

args = ["", "", "", ""]
count = 0
for i in tokens:
    print(i)
    args[count] = i
    print(args[count])
    count = count + 1
