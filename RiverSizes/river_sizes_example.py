# You are given a two-dimensional array of potentially unequal height and width.
# It contains only 0s and 1s. This array represents a map: 0s are land, and 1s are water.
# A "river" on this map consists of any number of contiguous, adjacent water squares,
# where "adjacent" means "above", "below", "to the left of", or "to the right of"
# (that is, diagonal squares are not adjacent).
#
# Write a function which returns an array of the sizes of all rivers represented in the input matrix.
# Note that these sizes do not need to be in any particular order.
#
# For example:
#
# const input = [
#   [1, 0, 0, 1, 0],
#   [1, 0, 1, 0, 0],
#   [0, 0, 1, 0, 1],
#   [1, 0, 1, 0, 1],
#   [1, 0, 1, 1, 0]
# ];
#
# riverSizes(input); // returns [1, 2, 2, 2, 5]


#
# Recursive method used to check the total number of adjacent 1's
# The prints will allow to understand how it python handles recursion
# https://pythontutor.com/visualize.html#mode=display is a great tool to test recursion
#
def check(row, col, matrix):
    print('Checking square: ' + str(row) + ',' + str(col))
    if row >= len(matrix) or row < 0 or col >= len(matrix[row]) or col < 0 or matrix[row][col] == 0 or matrix[row][col] == '^':
        return 0

    if matrix[row][col] == 1:
        matrix[row][col] = '^'
        print('Square ' + str(row) + ',' + str(col) + ' is 1 so we will check its sorroundings and then go back to previous if neccesary')
        value = 1 + check(row + 1, col, matrix) + check(row - 1, col, matrix) + check(row, col + 1, matrix) + check(row, col - 1, matrix)
        return value


#
# Method used to iterate all over the blocks
# We check adjacent blocks for each block using recursion in 'check' method
#
def getRiverSizes():
    _sizes = []

    for rowIndex in range(0, len(river_map)):
        for columnIndex in range(0, len(river_map[rowIndex])):
            if river_map[rowIndex][columnIndex] == 1:
                print('New check')
                new_size = check(rowIndex, columnIndex, river_map)
                _sizes.append(new_size)

    return _sizes


#
# Main script
#
if __name__ == '__main__':
    river_map = [[1, 0, 1, 1, 0],
                 [1, 0, 1, 0, 0],
                 [0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 1],
                 [1, 0, 0, 1, 0]]

    sizes = getRiverSizes()
    print(sizes)
