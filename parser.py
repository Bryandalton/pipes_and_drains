symbols = {
  "*": "SOURCE",
  "═": "HORIZONTAL",
  "║": "VERTICAL",
  "╝": "L_UP_LEFT",
  "╚": "L_UP_RIGHT",
  "?": "L_DOWN_LEFT",
  "?": "L_DOWN_RIGHT",
  "?": "T_UP",
  "╩": "T_DOWN",
  "╠": "T_LEFT",
  "╣": "T_RIGHT",
}
def read_file(arg):
    with open(arg, 'r', encoding='utf-8') as file:
        for line in file:
           parse_line(line.strip())

#get text as arg
def parse_line(txt):
    print(txt.split(' '))
    # for char in txt:
    #     print(char.split(' '))