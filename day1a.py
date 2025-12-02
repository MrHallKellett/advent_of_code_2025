from re import search, match, findall
from collections import Counter, defaultdict
from itertools import product, combinations, permutations
from math import inf as INF
from math import prod
from helpers import *

PP_ARGS = False, False #rotate, cast int

DAY = 1
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82///3"""

DEBUG = True


def solve(data):
    count = 0

    dial = 50
    for row in data:
        direction = row[0]
        val = int(row[1:])
        if direction == "L":
            dial -= val
        else:
            dial += val


        
        
        if dial <= 0:            
            dial = 100 + dial
        elif dial > 99:            
            dial = dial - 100
        if dial % 100 == 0:
            dial = 0
        
        

        if dial == 0:
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

        
