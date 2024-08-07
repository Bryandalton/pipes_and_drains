from parser import read_file
import sys

# make prettified maze array
# line break at max(x)
# every 3rd item is a new column
# looks like this:
# * ╣   ╔ ═ A
#   ╠ ═ ╝
#   C   ╚ ═ B

def main():
    #read the user input
    file_path = sys.argv[1]
    
    # parse it into a bag of pipes
    loose_pipes = read_file(file_path)

    grid_size = determine_grid_size(loose_pipes)

    # assembled maze from pipes
    maze_array = create_maze_array(loose_pipes, grid_size)

    # print it
    print_maze(maze_array, grid_size) 


## Make a flat representation of the maze
def create_maze_array(loose_pipes, grid_size):
    maze = []
    for row in range(grid_size[1]):
        for col in range(grid_size[0]):
            # if x = col && y = row: append piece else append " "
            pipe_result = find_pipe_at_pos(loose_pipes, col, row)
            maze.append(pipe_result)
    return maze
    

def find_pipe_at_pos(loose_pipes, col, row):
    for pipe in loose_pipes:
        if pipe['x'] == col and pipe['y'] == row:
            return pipe['piece']
    return " "

def determine_grid_size(loose_pipes):
    # print(loose_pipes)
    xvals = []
    yvals= []
    for i in loose_pipes:
        xvals.append(i.get('x') + 1)
        yvals.append(i.get('y') + 1)

    return (max(xvals), max(yvals))
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
       

if __name__ == "__main__":
    main()