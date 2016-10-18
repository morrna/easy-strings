import random as rnd

# chars[shift][hand][row][column]
dvorak_chars = [ [ [ [ 'b', 'm', 'w', 'v', 'z']
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

def easy_string( nchars, char_grid = dvorak_chars ):
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
