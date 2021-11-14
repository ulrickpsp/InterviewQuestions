# "Given an array A of length M and with N being the lenght of each subarray calculate the amount of steps
# (starting at location 0,0) needed to complete the path, until a location is repeated.
#
# A has the following format
#
# A = [[".", ".", ".", ".", ".", "x", "x", "x"],
#      [".", "x", ".", ".", ".", "x", "x", "."],
#      [".", ".", ".", "x", "x", "x", "x", "x"]]
#
# where every '.' means that the location is empty and a 'x' means that the location is occupied.
# The allowed steps are right, down, left, and up, always keeping that order.
# This is that if a right step cannot be done because location is occupied the down direction must be followed, an so on
#
# For example, for the given A in the example the following steps are done:
#
# [0, 1] [0, 2] [0, 3] [0, 4] [1, 4] [1, 3] [1, 2] [0, 2]
#
# Once we reach location [0,2] the path has been completed as we already occupied that location before.
# So the amount of steps to repeat a location is 8"

#
# Method used to check if valid movement
#
def can_move(row, row_index, column_index):
    try:
        _can_move = True if row[row_index][column_index] == '.' else False
    except IndexError:
        _can_move = False

    return _can_move


#
# Method used to simulate movements
#
def calculate_movements(A):
    movement_counter = 0
    positions_used = [[0, 0]]
    current_row = 0
    current_column = 0
    direction = 'R'
    completed = False

    while not completed:

        if direction == 'R':
            if can_move(A, current_row, current_column + 1):
                movement_counter += 1
                current_column += 1
                positions_used.append([current_row, current_column])
                print([current_row, current_column])
            else:
                direction = 'D'

        elif direction == 'D':
            if can_move(A, current_row + 1, current_column):
                movement_counter += 1
                current_row += 1
                positions_used.append([current_row, current_column])
                print([current_row, current_column])
            else:
                direction = 'L'

        elif direction == 'L':
            if can_move(A, current_row, current_column - 1):
                movement_counter += 1
                current_column -= 1
                positions_used.append([current_row, current_column])
                print([current_row, current_column])
            else:
                direction = 'U'

        elif direction == 'U':

            if can_move(A, current_row - 1, current_column):
                movement_counter += 1
                current_row -= 1
                positions_used.append([current_row, current_column])
                print([current_row, current_column])
            else:
                direction = 'R'

        if [current_row, current_column] in positions_used[:-1]:
            completed = True

    return movement_counter


#
# Main script
#
if __name__ == '__main__':
    A = [[".", ".", ".", ".", ".", "x", "x", "x"],
         [".", "x", ".", ".", ".", "x", "x", "."],
         [".", ".", ".", "x", "x", "x", "x", "x"]]
    movements = calculate_movements(A)
    print(movements)
