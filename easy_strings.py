#!/usr/bin/python3
import random as rnd

char_mats = {}

# chars[shift][hand][row][column]
char_mats['dvorak_chars'] = [ [ [ [ 'b', 'm', 'w', 'v', 'z']
                    ,[ 'd', 'h', 't', 'n', 's']
                    ,[ 'f', 'g', 'c', 'r', 'l']
                    ,[ '6', '7', '8', '9', '0']
                   ]
                  ,[ [ 'x', 'k', 'j', 'q', ';']
                    ,[ 'i', 'u', 'e', 'o', 'a']
                    ,[ 'y', 'p', '.', ',', "`"] # replacing quote marks because they seem dangerous
                    ,[ '5', '4', '3', '2', '1']
                   ]
                 ]
                ,[ [ [ 'B', 'M', 'W', 'V', 'Z']
                    ,[ 'D', 'H', 'T', 'N', 'S']
                    ,[ 'F', 'G', 'C', 'R', 'L']
                    ,[ '^', '&', '*', '(', ')']
                   ]
                  ,[ [ 'X', 'K', 'J', 'Q', ':']
                    ,[ 'I', 'U', 'E', 'O', 'A']
                    ,[ 'Y', 'P', '>', '<', '~'] # replacing quote marks because they seem dangerous
                    ,[ '%', '$', '#', '@', '!']
                   ]
                 ]
               ]

char_mats['qwerty_chars'] = [ [ [ [ 'n', 'm', ',', '.', '/']
                    ,[ 'h', 'j', 'k', 'l', ';']
                    ,[ 'y', 'u', 'i', 'o', 'p']
                    ,[ '6', '7', '8', '9', '0']
                   ]
                  ,[ [ 'b', 'v', 'c', 'x', 'z']
                    ,[ 'g', 'f', 'd', 's', 'a']
                    ,[ 't', 'r', 'e', 'w', "q"]
                    ,[ '5', '4', '3', '2', '1']
                   ]
                 ]
                ,[ [ [ 'N', 'M', '<', '>', '?']
                    ,[ 'H', 'J', 'K', 'L', ':']
                    ,[ 'Y', 'U', 'I', 'O', 'P']
                    ,[ '^', '&', '*', '(', ')']
                   ]
                  ,[ [ 'B', 'V', 'C', 'X', 'Z']
                    ,[ 'G', 'F', 'D', 'S', 'A']
                    ,[ 'T', 'R', 'E', 'W', 'Q']
                    ,[ '%', '$', '#', '@', '!']
                   ]
                 ]
               ]


def easy_string( nchars, char_grid = char_mats['dvorak_chars'] ):
    """
    randomly generate a string of length nchars which is easy to type
    """
    # rows and cols are completely random
    rows = [ rnd.randrange(4) for i in range(nchars) ]
    cols = [ rnd.randrange(5) for i in range(nchars) ]

    # start with shift on or off?
    shifts = [rnd.randrange(2)]
    charsleft = nchars - 1
    # shift stays the same for at least two chars
    switch_in = rnd.randrange(1, charsleft+1) 
    while charsleft > 0:
        if switch_in > 0:
            shifts.append(shifts[-1])
            switch_in -= 1
        else:
            shifts.append(1-shifts[-1])
            switch_in = rnd.randrange(1, charsleft+1)
        charsleft -= 1

    # for maximum speed, hands alternate when shift is off, and don't when shift is on.
    hands = []
    for i in range(nchars):
        if i == 0:
            hands.append(rnd.randrange(2))
        elif i > 0:
            if not (shifts[i-1] or shifts[i]):
                hands.append(1-hands[i-1])
            else:
                hands.append(hands[i-1])

    # assemble the string
    ezs = ''
    for s, h, r, c in zip(shifts, hands, rows, cols):
        ezs += char_grid[s][h][r][c]

    return ezs


if __name__=="__main__":
    import argparse

    default_charset = 'dvorak_chars'

    parser = argparse.ArgumentParser(description="Generate easily typed strings")

    parser.add_argument("-n", default=1, type=int, \
                        help = "Number of strings to generate (default 1)")
    parser.add_argument("-l", default=12, type=int, \
                        help = "Length of generated strings (default 12)")
    parser.add_argument('-q', '--qwerty', dest='charset', action='store_const', \
                        const='qwerty_chars', default=default_charset, \
                        help = "Base the password on the QWERTY keyboard layout")
    parser.add_argument('-d', '--dvorak', dest='charset', action='store_const', \
                        const='dvorak_chars', default=default_charset, \
                        help = "Base the password on the Dvorak keyboard layout")
    
    args = parser.parse_args()

    for i in range(args.n):
        print(easy_string(args.l, char_grid=char_mats[args.charset] ))

