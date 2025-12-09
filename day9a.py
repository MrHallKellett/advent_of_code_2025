from re import search, match, findall
from collections import Counter, defaultdict
from itertools import product, combinations, permutations
from math import inf as INF
from math import prod
from helpers import *

PP_ARGS = False, False #rotate, cast int

DAY = 9
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3///aa
"""

DEBUG = True


def solve(data):
    count = 0

    column_map = {}
    column_map.setdefault([])
    row_map = {}
    row_map.setdefault([])

    for row in data:
        x,y = list(map(int, row.split(",")))
        rect = (x, y)
        row_map[x].append(rect)
        row_map[x] = sorted(row_map[x], key=lambda x: x[1])
        column_map[y].append(rect)        
        column_map[y] = sorted(column_map[y])


    

    # go through every point as p1.
    for current_x, points_on_this_row in row_map.items():

        for index, p1 in enumerate(points_on_this_row):

            # find p2 by + 1 index in the row_map.
            p2 = row_map[current_x][index + 1]

            # find p3 by + 1 index of p2 in the column_map

    # find p4 by - 1 index of p2 in the row_map


           

        




        

        

        
    

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

        
