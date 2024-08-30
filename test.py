import unittest
import sys
from grid import find_source, find_left_of_index, find_right_of_index, find_down_of_index, find_up_of_index
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

    # 6 7 8
    # 3 4 5
    # 0 1 2 Grid is bae
arr = [0,1,2,3,4,5,6,7,8]

#write unit tests for up down and right

#@unittest.skip("Skipping this test.")


class TestMathOperations(unittest.TestCase):
    def test_find_source(self):
        self.assertEqual(find_source([]),-1,"When given empty list should not find a source")
        self.assertEqual(find_source(['*']), 0 ,"When given a list should find a source")
        self.assertEqual(find_source(['A','B','*']),2,"When given a list should find a source")
    
    def test_find_left_of_index(self):
        self.assertEqual(find_left_of_index(0, 1), -1 ,"identifies if nothing left of index")
        self.assertEqual(find_left_of_index(1, 2), 0 ,"returns value left of *")
        self.assertEqual(find_left_of_index(0, 2), -1 ,"identifies if nothing left of source")

        self.assertEqual(find_left_of_index(1, 1), -1 ,"returns value left of single column")

    def test_find_right_of_index(self):
        # 6 7 8
        # 3 4 5
        # 0 1 2 Grid is bae
        self.assertEqual(find_right_of_index(4,3), 5,"5 is right of 4 in grid")
        self.assertEqual(find_right_of_index(5,3), -1,"there is nothing there")
    @unittest.skip("Skipping this test.")
    def test_find_up_of_index(self):
        # 6 7 8
        # 3 4 5
        # 0 1 2 Grid is bae
        self.assertEqual(find_up_of_index(4,3), 7, "7 is up of 4")
        self.assertEqual(find_up_of_index(8,3), -1,"nothing is up of 8")
    @unittest.skip("Skipping this test.")
    def test_find_down_of_index(self):
        # 6 7 8
        # 3 4 5
        # 0 1 2 Grid is bae
        self.assertEqual(find_up_of_index(4,3), 1, "1 is down of 4")
        self.assertEqual(find_up_of_index(0,3), -1, "nothing is down of 0")



if __name__ == '__main__':
    unittest.main()