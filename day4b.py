from re import search, match, findall
from collections import Counter, defaultdict
from itertools import product, combinations, permutations
from math import inf as INF
from math import prod
from helpers import *

PP_ARGS = False, False #rotate, cast int

DAY = 4
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.///43
"""

DEBUG = True


def found_toilet_roll(data, ox, oy):
    s = ""
    print(f"""
          FOUND GOOD TOILET ROLL AT {ox} {oy}
          """)

    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if x == ox and y == oy:
                c = "x"
            else:
                c = data[y][x]
            s += c
        s += "\n"
    print(s)
    input()

def solve(data):
    count = 0

    MAX_ROLLS = 4
    TOILET_ROLL = "@"

    data = [list(row) for row in data]

    width, height = len(data[0]), len(data)
    
    removal = True

    while removal:
        removal = False

        for y in range(height):
            for x in range(width):

                if data[y][x] != TOILET_ROLL:
                    continue

                roll_count = 0
                for yc, xc in ((-1, -1),
                            (0, -1),
                            (1, -1),
                            (1, 0),
                            (1, 1),
                            (0, 1),
                            (-1, 1),
                            (-1, 0)):
                    
                    nx, ny = x + xc, y + yc

                    if nx < 0 or nx >= width:
                        continue
                    if ny < 0 or ny >= height:
                        continue

                    if data[ny][nx] == TOILET_ROLL:
                        roll_count += 1
                
                if roll_count < MAX_ROLLS:
                    count += 1
                    data[y][x] = "."
                    removal = True
            

        
    

    return count




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    try:
        if p.check(TESTS, solve):
            puzzle_input = p.load_puzzle()
            puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
            print("FINAL ANSWER: ", solve(puzzle_input))
    except Exception as e:
        p.log.close()
        raise e

        
