from re import search, match, findall
from collections import Counter, defaultdict
from itertools import product, combinations, permutations
from math import inf as INF
from math import prod
from helpers import *

PP_ARGS = False, False #rotate, cast int

DAY = 6
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + ///3263827
"""

DEBUG = True


def solve(data):
    total = 0
    nums = []
    ops = []
    get_ops = False

    data = [list(row) for row in data]
    
    finished = False
    math = ""
    while not finished:
        new_col = ""
        data_left = False
        for row in data:
            try:
                new_col += row.pop(-1)
                data_left = True
            except IndexError:
                pass
            
            

        if not data_left:
            finished = True
                
        if new_col.strip() == "" or finished:
            op = "*" if "*" in math else "+"
            math = math.replace(op, " ")
            math = op.join(math.split())
            print(f"The math was {math}")
            total += eval(math)
            math = ""
        else:
            math += new_col
            
        
        

    


                
    print("Total is", total)
    
        

        
    

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

        
