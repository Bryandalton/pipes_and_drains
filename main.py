from parser import read_file 
import sys

def handle_blank():
    pass



def create_maze(loose_pipes):
    grid_size = determine_grid_size(loose_pipes)

    for col in range(grid_size[0]):
        for row in range(grid_size[1]):
            print(col, row)



    # print(loose_pipes)
    pass

def main():
    file_path = sys.argv[1]
    loose_pipes = read_file(file_path)
    create_maze(loose_pipes)

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

