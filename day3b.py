from re import search, match, findall
from collections import Counter, defaultdict
from itertools import product, combinations, permutations, combinations_with_replacement
from math import inf as INF
from math import prod
from helpers import *
from itertools import permutations

PP_ARGS = False, False #rotate, cast int

DAY = 3
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """987654321111111
811111111111119
234234234234278
818181911112111///3121910778619
"""

DEBUG = True


def solve(data):
    total = 0

    max_length = len(max(data, key=len))

    for row in data:
        needed = 12
        orig_row = row
        all_indices = []
        print("ROW IS", row)
        finished = False
  
        final = ""
        while len(final) != needed:

            for search_digit in range(9, -1, -1):
                search_digit = str(search_digit)
                print("Searching for", search_digit)
                for i in range(len(row)-1, -1, -1):

                    check_digit = row[i]
                    print("check against", check_digit)
                    if check_digit == search_digit:
                        final = final + search_digit
                        row = row[:i]
                        print("Final is now", final)
                        print("Reducing search space to", row)
                        input()

                    
        print(f"In {orig_row}, the largest joltage can be found to produce {final}.")
        total += int(final)
        
        



        


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

        
