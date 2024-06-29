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
#
def find_source( symbol, x, y):
    if symbol == 'ast':
        source = (x,y)
    return source

def find_connection(symbol, x, y):
    pass

def find_sink(symbol, connection):
    if symbol is str & connection:
        return symbol
