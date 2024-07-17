from parser import read_file 
import sys


def main():
    file_path = sys.argv[1]
    loose_pipes = read_file(file_path)
    print(loose_pipes)

if __name__ == "__main__":
    main()

