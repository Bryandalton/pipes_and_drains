from parser import read_file 
import sys


def main():
    file_path = sys.argv[1]
    read_file(file_path)

if __name__ == "__main__":
    main()

