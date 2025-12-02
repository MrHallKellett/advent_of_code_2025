from re import search, match, findall
from collections import Counter, defaultdict
from itertools import product, combinations, permutations
from math import inf as INF
from math import prod
from helpers import *

PP_ARGS = False, False #rotate, cast int

DAY = 2
TEST_DELIM = "---"
FILE_DELIM = ","
TESTS = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124///4174379265
"""

DEBUG = True

def invalid_id(data):
    data = str(data)

    for j in range(0, len(data)):
        chunk = data[:j+1]
        for x in range(2, 10):
            if chunk * x == data:
                return True
    return False



def solve(data):
    tot = 0
    for row in data:
        first, last = row.split("-")
        for id in range(int(first), int(last)+1):
            if invalid_id(id):               
                
                tot += int(id)


    return tot




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

        
