from parser import read_file 
import sys

#make prettified maze array
#line break at max(x)
#looks like this:
# * ╣   ╔ ═ A
#   ╠ ═ ╝    
#   C   ╚ ═ B

def handle_blank():
    pass

def find_pipe_at_pos(loose_pipes, col, row):
    for pipe in loose_pipes:
        if pipe['x'] == col and pipe['y'] == row:
            return pipe['piece']
    return " "

def create_maze_array(loose_pipes):
    grid_size = determine_grid_size(loose_pipes)
    maze = []
    for col in range(grid_size[0]):
        for row in range(grid_size[1]):
            #if x = col && y = row: append piece else append " "
            pipe_result = find_pipe_at_pos(loose_pipes, col, row)
            # maze.append(f'{col} {row}')
            maze.append(pipe_result)
    return maze

def main():
    file_path = sys.argv[1]
    loose_pipes = read_file(file_path)
    maze_array = create_maze_array(loose_pipes)
    print(maze_array)
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

