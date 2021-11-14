# A company focused on building blocks so that the snake from 'SnakeMovement' example can move, keeps track of their
# movements for each year. They think it's a good thing to make up the numbers so they're never in negative numbers.
#
# Let's say they provide us the following list of movements:
#
#   movements = [10, -10, 20, -30, -40, 70, -25, 30, 50]
#
# We're allowed to push any movement to the end to achieve the goal of maintaining a balance greater or equal to 0
# Asume that the sum of all movements is always greater than 0
# They ask us which is the minimum number of movements needed to achieve this goal
#
# So, in this example we would end up having this list:
#
#   output = [10, -10, 20, 70, -25, 30, 50, -30, -40]
#   Movements = 2


#
#   Method used to find the minimum amount of movements needed
#
def find_number_of_movements(_movements):

    balance_sum = 0
    changes = 0
    for i in range(0, len(_movements)):
        if balance_sum + _movements[i] >= 0:
            balance_sum += _movements[i]
        else:
            changes += 1

    return changes


#
# Main script
#
if __name__ == '__main__':
    movements = [10, -50, 30, -45, 70, -120, 165, -300, 50, 10, -50, 30, -45, 70, -520, 510, -300, 50]
    output = find_number_of_movements(movements)
    print(output)

