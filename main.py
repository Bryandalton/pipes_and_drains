from parser import read_file
from printer import print_maze
import sys

#move print function and dependencies to own file and call into main
#make a scripts folder for parser and printer


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


# Make a flat representation of the maze
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



if __name__ == "__main__":
    main()