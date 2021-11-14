# Check if sequence is a sublist of array
# True; if every integer in sequence is present in array maintaining the same order
# False; otherwise
#
# Example 1:
#
#     array = [1, 3, 4, 16, 24, 5]
#     sequence = [1, 4, 24]
#     output = True
#
# Example 2:
#
#     array = [1, 3, 4, 16, 24, 5]
#     sequence = [1, 4, 25]
#     output = False


#
# Method used to check if a sequence is in an array
# O(n) time | O(1) space where n is the length of the array
#
def check_sequence_in_array(_array, _sequence):

    seq_elements = 0
    arr_index = 0

    # Iterate all elements in sequence
    for seq_index in range(0, len(_sequence)):

        # Iterate from last index to the end
        for arr_index in range(arr_index, len(_array)):

            # If there's a match, increase seq_elements counter
            # Also update the value of the array index (if we are at the last position don't do anything)
            if _sequence[seq_index] == array[arr_index]:
                arr_index = arr_index if arr_index == len(_array) - 1 else arr_index + 1
                seq_elements += 1
                break

    # Check if length of sequence is the same as the number of equal elements found
    return len(sequence) == seq_elements


#
# Main script
#
if __name__ == '__main__':
    array = [1, 3, 4, 16, 24, 5]
    sequence = [1, 4, 25]
    isValid = check_sequence_in_array(array, sequence)
    print(isValid)
