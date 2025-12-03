from re import search, match, findall
from collections import Counter, defaultdict
from itertools import product, combinations, permutations
from math import inf as INF
from math import prod
from helpers import *

PP_ARGS = False, False #rotate, cast int

DAY = 3
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """987654321111111
811111111111119
234234234234278
818181911112111///357
"""

DEBUG = True


def solve(data):
    total = 0

    upper = max(map(int, data))

    for row in data:
        
        for comb in range(99, 9, -1):
            
            
            x, y = list(str(comb))
            result = search(f"{x}[1-9]*{y}", row)
            if result is not None:
                
                total += comb
                print(f"In {row}, you can make the largest joltage possible, {comb},")
                break

    return total




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

        
