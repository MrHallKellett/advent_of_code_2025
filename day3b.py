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
        all_indices = []
        print("ROW IS", row)
        finished = False
        for digit in range(9, 0, -1):
            digit = str(digit)

            these_indices = sorted([max_length-i-1 for i, v in enumerate(reversed(row)) if v == digit], reverse=True)

            print(f"These are the indicies of {digit}: {these_indices}")

            input()

            for index in these_indices:
                if len(all_indices) < 12:
                    all_indices.append(index)
                else:

                    all_indices = sorted(all_indices[:12])

                    print("indicies in order are: ")
                    print(all_indices)
                    

                    number = int("".join([row[i] for i in all_indices]))
                    
                    print(f"In {row}, the largest joltage can be found to produce {number}.")
                    total += number
                    input()
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

        
