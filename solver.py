def main():
    """ This function asks user to input a Sudoku grid and prints
the solved grid by calling the display() function """

    grid = input("Welcome! Please input a Sudoku grid following the instructions in the ReadMe file >>> ") 
    print "\nBelow is the solved Sudoku puzzle:\n" + display(solveSudoku(grid))

def display(grid):
    """ This function displays solved puzzle in human-readable format """
    solved = "" # initialize "solved grid" to empty string
    for x in range(9): # repeats 9 times for each subarray
        if x%3 == 0: # appends linebreak to every 3 rows
            solved += "_"*30 + "\n"
        for y in range(9): # repeats 9 times for each element in subarray
                solved += " " + str(grid[x][y]) + " " # appends value to "solved grid"
                if (y+1)%3 == 0: # appends separater to line wto every 3 cell values
                    solved += "|"
        solved += "\n" # creates new line after every row in puzzle appended
    return solved # return "solved grid"

def notSolved(grid):
    """ This function determines if puzzle is solved. Returns True
if not solved. Returns False is solved. """
    for x in range(9): # repeats 9 times for each row in puzzle
        for y in range(9): # repeats 9 times for each column in puzzle
            if grid[x][y] == 0: # if 0 found in any cell, return True
                return True 
    return False # if 0 not found in any cell, return False

def solveSudoku(grid):
    """ This function solves the puzzle by calling
the possibilities() function """
    while notSolved(grid): # while the puzzle is not solved
        for x in range(9): # repeats for 9 times for every row
            for y in range(9): # repeats 9 times for every column
                if grid[x][y] == 0: # if cell value equals 0
                    possibilities = possibility(grid, x, y)
                    if len(possibilities) == 1:
                        # if there is only one possibility in cell,
                        # set cell (x,y) to possibility value
                        grid[x][y] = possibilities[0]
    return grid # return solved puzzle

def row(grid, x):
    """ This function returns all the values in
the specified cell's row. These are values that
the cell cannot be """
    gridRow = [] # list of values in cell's row initialized
    # every value in cell's row not equal to 0 is appended to list
    for value in grid[x]: 
        if value != 0: 
            gridRow.append(value)
    return gridRow # return list

def column(grid, y):
    """ This function returns all the values in
the specified cell's column. These are values
that the cell cannot be """
    gridColumn = [] # list of values in cell's column initialized
    for value in range(9):
        # every value in cell's column not equal to 0 is appended to list
        if grid[value][y] != 0:
            gridColumn.append(grid[value][y])
    return gridColumn # return list

def box(grid, x, y):
    """ This function returns all the values in
the specified cell's box. These are values that
the cell cannot be """
    topX = (x/3)*3 # obtains x value of first cell in box
    topY = (y/3)*3 # obtains y value of first cell in box
    gridBox = [] # list of values in cell's box initialized
    for row in range(topX, topX+3): # repeats 3 times 
        for column in range(topY, topY+3): # repeats 3 times
            if grid[row][column] != 0:
                # every value in cell's box not equal to 0 is appended to list
                gridBox.append(grid[row][column])
    return gridBox # return list

def possibility(grid, x, y):
    """ This function determines all the possibilities of the specified cell value by calling
the row(), column(), and box() functions """
    possible = [] # list of possible values initialized
    for num in range(1, 10): # repeats 9 times from 1 to 9 inclusive
        # if number not found in any of three lists, number is appended to "possible" list
        if (num not in row(grid, x)) and (num not in column(grid, y)) and (num not in box(grid, x, y)):
            possible.append(num)
    return possible # list of possible values returned

main()
