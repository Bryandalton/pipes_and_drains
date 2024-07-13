import unittest
import sys
# * ╣   ╔ ═ A
#   ╠ ═ ╝    
#   C   ╚ ═ B

#coord map x:y
# * 0 2
# C 1 0
# ╠ 1 1
# ╣ 1 2
# ═ 2 1
# ╚ 3 0
# ╝ 3 1
# ╔ 3 2
# ═ 4 0
# ═ 4 2
# B 5 0
# A 5 2

#there is only one ast can be anywhere on the grid
#there are 10 different pipes with either 2 or 3 connects
#there are 2 types of straight pipes
#there are 4 types of right angle pipes
#there are also 4 T shaped pipes
#any letter A - Z are possible also all letters connect to adjoining letters

#approach
#construct the map
#very simple map: * ═ A
#parse the *
#parse the pipes and Drains
#find symbol determine connection directions
#if symbols have a matching connection connected = true

#possible directions:
# up = (x, y + 1)
# down = (x, y - 1)
# left = (x -1, y)
# right = (x + 1, y)

# create the grid starting with y = 0 and looping through all x values
#the increment y and repeat loop until y = input[length -1]

print(sys.argv)

def create_grid():
    maze: dict[str, tuple[int,int]] = {}
    pass

def simp_add (n,i):
    return n + i

def find_source( symbol, x, y):
    if symbol == 'ast':
        source = (x,y)
    return source

def find_connection(symbol, x, y):
    pass

def find_sink(symbol, connection):
    if symbol is str & connection:
        return symbol


# class TestMathOperations(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(simp_add(1, 2), 3)
#         self.assertEqual(simp_add(-1, 1), 0)
#         self.assertEqual(simp_add(-1, -1), 3, "Adding negative number should return negative result")

# if __name__ == '__main__':
#     unittest.main()