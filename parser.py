symbols = {
    "*": "SOURCE",
    "═": "HORIZONTAL",
    "║": "VERTICAL",
    "╝": "L_UP_LEFT",
    "╚": "L_UP_RIGHT",
    "╔": "L_DOWN_LEFT",
    "╗": "L_DOWN_RIGHT",
    "╦": "T_UP",
    "╩": "T_DOWN",
    "╠": "T_LEFT",
    "╣": "T_RIGHT",
}

# piece = {
#     "piece": 'SOURCE',
#     "x": 0,
#     "y": 0
# }


def get_symbol(str):
    if str in symbols:
        return symbols[str]
    else:
        return str


def read_file(arg):
    pipes = []
    with open(arg, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip() == '':
                continue
            pipes.append(parse_line(line.strip()))

    return pipes
# get text as arg


def parse_line(txt):
    parsed_array = txt.split(' ')
    new_piece = {
        "piece": get_symbol(parsed_array[0]),
        'x': int(parsed_array[1]),
        'y': int(parsed_array[2])
    }
    return new_piece
