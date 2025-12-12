from re import search, match, findall
from collections import Counter, defaultdict
from itertools import product, combinations, permutations
from math import inf as INF
from math import prod
from helpers import *

import numpy as np

PP_ARGS = False, False #rotate, cast int

DAY = 12
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2///2
"""

DEBUG = True


class Present:

    def __init__(self, shape):
        self.data = np.array([list(row) for row in shape.splitlines()])

    def rotate(self, n):
        return np.rot90(self.data, k=n)
    
    def display(self):
        for row in self.data:
            print("".join(row))
    
    def get_bin(self):
        
        data = "".join("".join(row) for row in self.data)
        return int(data.replace("#", "1").replace(".", "0"), 2)


class Region:

    

    def __init__(self, data):
        data = data.replace(":", "").split()
        self.w, self.h = list(map(int, data[0].split("x")))
        self.required = list(map(int, data[1:]))

        self.binary = 0
        
    
    def check_presents(self, presents):

        # every location
        # go through every rotation

            # go through every present

                # 


        

def solve(data):
    count = 0

    shape_data = []
    regions = []
    presents = []

    region_mode = False

    for row in data:
        if not row:
            continue
        if row.endswith(":"):
            shape_data.append([])
        elif "#" in row:
            shape_data[-1].append(row)
        else:
            regions.append(Region(row))


    for shape in shape_data:

        presents.append(Present("".join(shape)))
        
    for i, region in enumerate(regions):

        print(f"Region {i+1}")

        region.check_presents(presents)

        

        
    

    return count




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    test_shape = '''###
#..
###'''

    x = Present(test_shape)


    
    

    for _ in range(4):
        x.rotate(1)
        x.display()
        print(x.get_bin())


    input()



    try:
        if p.check(TESTS, solve):
            puzzle_input = p.load_puzzle()
            puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
            print("FINAL ANSWER: ", solve(puzzle_input))
    except Exception as e:
        p.log.close()
        raise e

        
