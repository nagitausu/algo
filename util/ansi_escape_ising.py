import time
import random
import math

SEQ = '\033[{}m{{}}\033[0m'

fgcodes = {
    None            : 39, 'black'         : 30, 'red'           : 31,
    'green'         : 32, 'yellow'        : 33, 'blue'          : 34,
    'magenta'       : 35, 'cyan'          : 36, 'light gray'    : 37,
    'dark gray'     : 90, 'light red'     : 91, 'light green'   : 92,
    'light yellow'  : 93, 'light blue'    : 94, 'light magenda' : 95,
    'light cyan'    : 96, 'white'         : 97
}

bgcodes = {
    None            : 49, 'black'         : 40, 'red'            : 41,
    'green'         : 42, 'yellow'        : 43, 'blue'           : 44,
    'magenta'       : 45, 'cyan'          : 46, 'light gray'     : 47,
    'dark gray'     : 100, 'light red'    : 101, 'light green'   : 102,
    'light yellow'  : 103, 'light blue'   : 104, 'light magenda' : 105,
    'light cyan'    : 106, 'white'        : 107
}

stylecodes = {
    'bold'       : 1, 'dim'        : 2, 'underlined' : 4, 'blink'      : 5,
    'reverse'    : 7, 'hidden'     : 8,
}

def prettify(string,fg=None,bg=None,*styles):
    try:
        if styles:
            code = '{};{};{}'.format(
                ';'.join(map(lambda x:str(stylecodes[x]), styles)),
                fgcodes[fg],bgcodes[bg])
        else:
            code = "{};{}".format(fgcodes[fg], bgcodes[bg])
    except KeyError as e:
        raise ValueError("style or color not supported: \n{}".format(e))
    return SEQ.format(code).format(string)

def bold(string):
    return SEQ.format(stylecodes['bold']).format(string)

def underlined(string):
    return SEQ.format(stylecodes['underlined']).format(string)

if __name__ == "__main__":
    N = 30
    field = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            field[i][j] = random.randrange(0, 2)
            if field[i][j] == 0:
                field[i][j] = -1
    T = 2.5
    print("")
    while True:
        for i in range(800):
            x = random.randrange(0, N)
            y = random.randrange(0, N)
            states = field[x][(y+1) % N] + \
                     field[x][y-1] + \
                     field[x-1][y] + \
                     field[(x+1) % N][y]
            p = 1.0 / (1.0 + math.exp(2.0 * states / T))
            if random.random() <= p:
                field[x][y] = -1
            else:
                field[x][y] = 1
        msg = ""
        for i in range(N):
            for j in range(N):
                val = field[i][j]
                if val == -1:
                    msg += prettify(" 1", 'dark gray', 'light gray')
                else:
                    msg += prettify(" 0", 'light gray', 'dark gray')
            msg += "\n"

        # Hide cursor while printing canvas to avoid flickering
        msg = "\033[?25l" + msg + "\033[?25h"
        print(msg)

        time.sleep(0.001)

        # Move cursor up
        print("\033[" + str(N+1) + "A", end="")
