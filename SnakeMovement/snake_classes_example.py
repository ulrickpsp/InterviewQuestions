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
# This class represents each of the items in the matrix
#
class Block:
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.occupied = True if value == 'x' else False
        self.previously_used = True if row == 0 and column == 0 else False


#
# This class represents the animal moving around the blocks
#
class Snake:
    def __init__(self, _blocks):
        self.direction = 'R'
        self.current_row = 0
        self.current_column = 1
        self.blocks = _blocks
        self.total_movements = 0

    #
    #   Method used to determine the new direction:  Right -> Down -> Left -> Up -> Right
    #
    def update_direction(self):
        self.direction = 'D' if self.direction == 'R' else \
            'L' if self.direction == 'D' else \
                'U' if self.direction == 'L' else \
                    'R'

    #
    # Method used to get the potential new position of the snake based on current direction
    #
    def get_next_position(self):

        # Update values for next iteration
        next_column = self.current_column + 1 if self.direction == 'R' else \
            self.current_column - 1 if self.direction == 'L' else \
                self.current_column

        next_row = self.current_row + 1 if self.direction == 'D' else \
            self.current_row - 1 if self.direction == 'U' else \
                self.current_row

        return next_row, next_column

    #
    # Method used to simulate the movement
    # Note that movement ends when the snake goes back to a previously used block
    # Returns true if that happens, false otherwise
    def try_move(self):

        # Check the condition to finish movements or make a new movement
        if self.blocks[self.current_row][self.current_column].previously_used is True:

            # Movement finished
            _completed = True

        else:

            # Movement not finished
            _completed = False

            # Calculate next block
            next_row, next_column = self.get_next_position()

            # Check margins in columns and rows
            # Check if block is occupied
            if len(self.blocks) > next_row >= 0 \
                and len(self.blocks[self.current_row]) > next_column >= 0 \
                    and not self.blocks[next_row][next_column].occupied:

                # Set block is occupied
                self.blocks[self.current_row][self.current_column].previously_used = True

                # Increase number of movements done
                self.total_movements += 1

                # Update values for next iteration
                self.current_row = next_row
                self.current_column = next_column
                print("Next location is " + str([self.current_row, self.current_column]))

            else:
                self.update_direction()

        return _completed


#
# Method used to initialize the block objects
#
def generate_blocks(matrix):
    _blocks = []
    for row in range(0, len(matrix)):
        row_data = []
        for column in range(0, len(matrix[row])):
            row_data.append(Block(row, column, matrix[row][column]))

        _blocks.append(row_data)

    return _blocks


#
# Method used to print to console the route followed
# x -> obstacle
# . -> not used block
# ✓ -> used block
#
def print_route():
    for row in range(0, len(snake.blocks)):
        column_data = ''
        for column in range(0, len(snake.blocks[row])):

            if snake.blocks[row][column].occupied is True:
                column_data += "x"
            elif snake.blocks[row][column].previously_used is True:
                column_data += "✓"
            else:
                column_data += "."
        print(column_data)


#
# Main script
#
if __name__ == '__main__':

    completed = False
    A = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "x", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "x", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", "x", ".", "x", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "x", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

    snake = Snake(generate_blocks(A))
    while not completed:
        completed = snake.try_move()

    print('Total number of movements = ' + str(snake.total_movements))
    print_route()

