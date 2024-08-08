def print_maze(maze_array, grid_size):
    # convert it into a matrix so we can print it
    maze_matrix = create_maze_matrix(maze_array, grid_size)
    
    aligned_mazed = correct_maze_matrix(maze_matrix)
    for row in aligned_mazed:
        print(' '.join(row))

# reverse the rows of the maze for better printing
def correct_maze_matrix(unaligned_maze):
   aligned_maze = []
   for row in unaligned_maze[::-1]:
       aligned_maze.append(row)
   return aligned_maze
       
# take the flat maze, and turn it into a 2d matrix
# but its backwards!
def create_maze_matrix(maze_array, grid_size):
    maze_matrix = []
    start = 0
    end = len(maze_array)
    # print(grid_size[0])
    step = grid_size[0]
    for i in range(start, end, step):
        x = i
        maze_matrix.append(maze_array[x:x+step])

    return maze_matrix

