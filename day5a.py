from re import search, match, findall
from collections import Counter, defaultdict
from itertools import product, combinations, permutations
from math import inf as INF
from math import prod
from helpers import *

PP_ARGS = False, False #rotate, cast int

DAY = 5
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """3-5
10-14
16-20
12-18

1
5
8
11
17
32///3
"""

DEBUG = True


def solve(data):
    count = 0

    ranges = set()

    for row in data:
        if not row: continue
        if "-" in row:
            start, stop = list(map(int, row.split("-")))
            stop += 1
            ranges.add(range(start, stop))
        else:
            if any(int(row) in r for r in ranges):
                count += 1
        

        
    

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

        
