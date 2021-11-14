# Given an unsorted array A find a sublist so that if we sorted this sublist the whole list would be sorted.
# Return the starting index and end index of the sublist
#
# For example if A = {0, 1, 3, 7, 5, 3, 1, 9, 13, 24, 31, 47 ,52}
# If we sorted the sublist (3, 7, 5, 3, 1, 9) -> (1, 3, 3, 5, 7, 9)
# Then, the whole list would be sortered {0, 1 (1, 3, 3, 5, 7, 9), 13, 24, 31, 47 ,52}
# So the indexes we're looking for are 2 and 7


def find_sublist_indexes(unsorted_list):
    # Local vars initialization
    first_index = -1
    last_index = -1

    # Get the sorted list
    sorted_lst = sorted(unsorted_list)

    # A valid strategy would be to compare the changes between the list and the ordered list
    # First index is only updated the first time
    # Last index is updated until the last different element
    for i in range(0, len(unsorted_list)):
        if sorted_lst[i] != unsorted_list[i]:
            if first_index == -1:
                first_index = i
            else:
                last_index = i

    # Return data protecting against arrays of length = 1
    return (0, 0) if first_index == -1 and last_index == -1 else (first_index, last_index)


#
# Main script
#
if __name__ == '__main__':
    A = [16, 2, 3, 17, 18, 3]
    output = find_sublist_indexes(A)
    print(output)
