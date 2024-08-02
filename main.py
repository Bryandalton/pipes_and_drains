from parser import read_file
import sys

# make prettified maze array
# line break at max(x)
# every 3rd item is a new column
# looks like this:
# * ╣   ╔ ═ A
#   ╠ ═ ╝
#   C   ╚ ═ B


def find_pipe_at_pos(loose_pipes, col, row):
    for pipe in loose_pipes:
        if pipe['x'] == col and pipe['y'] == row:
            return pipe['piece']
    return " "


def create_maze_array(loose_pipes):
    grid_size = determine_grid_size(loose_pipes)
    maze = []
    for row in range(grid_size[1]):
        for col in range(grid_size[0]):
            # if x = col && y = row: append piece else append " "
            pipe_result = find_pipe_at_pos(loose_pipes, col, row)
            # maze.append(f'{col} {row}')
            maze.append(pipe_result)
    return maze


def corrected_maze_matrix(loose_pipes):
   unaligned_maze = print_maze(loose_pipes)
   aligned_maze = []
   for row in unaligned_maze[::-1]:
       aligned_maze.append(row)
   return aligned_maze
       
    
   
       



#breaks every 3 items into their own arrays
#would be correct if rotated -90deg
def print_maze(loose_pipes):
    maze_matrix = []
    maze_array = create_maze_array(loose_pipes)
    start = 0
    end = len(maze_array)
    step = 6
    for i in range(start, end, step):
        x = i
        maze_matrix.append(maze_array[x:x+step])

    return maze_matrix


def main():
    file_path = sys.argv[1]
    loose_pipes = read_file(file_path)
    # maze_array = create_maze_array(loose_pipes)
    show_maze = print_maze(loose_pipes)
    maze = corrected_maze_matrix(loose_pipes)
    for row in maze:
        print(row)





def determine_grid_size(loose_pipes):
    # print(loose_pipes)
    xvals = []
    yvals= []
    for i in loose_pipes:
        xvals.append(i.get('x') + 1)
        yvals.append(i.get ('y') + 1)

    return (max(xvals), max(yvals))



if __name__ == "__main__":
    main()

