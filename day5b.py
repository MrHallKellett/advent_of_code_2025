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
32///14
"""

DEBUG = True

class Range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __repr__(self):
        return f"{self.start}-{self.stop}"

    def count(self):
        return self.stop - self.start

    def update(self, other):
        merge = False
        if other.start <= self.stop and other.start >= self.start:
            self.stop = other.stop
            merge = True
        elif other.stop >= self.start and other.stop <= self.stop:
            self.start = other.start
            merge = True
        
        if merge:
            print(f"Merging {self} with {other}")
        return merge

def solve(data):
    count = 0

    ranges = []

    for row in data:
        if not row: continue
        if "-" in row:
            start, stop = list(map(int, row.split("-")))
            new_range = Range(start, stop)             
            ranges.append(new_range)

     
    

    merge = True
    while merge:
        merge = False
        i = 0
        while not merge and i < len(ranges):
            j = 0
            r1 = ranges[i]
            while not merge and j < len(ranges):
                r2 = ranges[j]
            
                if r1 == r2:    continue

                if r1.update(r2):
                    remove_this_range = r2
                    merge = True
                
                j += 1
            i += 1
        
        if merge:
            ranges.remove(remove_this_range)



    

    return sum(r.count() for r in ranges)




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

        
