def find_source(maze_array):
    for i in range(len(maze_array)):
        if maze_array[i] == "*":
            return i
    return -1

def find_left_of_index( index, num_columns):
    if index % num_columns == 0:
        return -1
    return index - 1

def find_right_of_index(index, num_columns):
    pass

def find_up_of_index(index, num_columns):
    pass

def find_down_of_index(index, num_columns):
    pass