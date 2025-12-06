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

DEBUG = False

class Range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __repr__(self):
        return f"{self.start}-{self.stop}"

    def count(self):
        return self.stop - self.start + 1
    


    def merge_and_get_deleted(self, other):
        p.bugprint(f"comparing {self} against {other}")
        if other.start > self.stop:
            p.bugprint("other lies completely to the right of me")
            return None
        # other lies completely to the right of me
        elif other.stop < self.start:
            p.bugprint("other lies completely to the left of me")
            return None
        # other is completely contained within me
        elif other.start >= self.start and other.start <= self.stop and other.stop >= self.start and other.stop <= self.stop:
                p.bugprint("# other is completely contained within me")
                return other
        # other is completely contained within me
        elif self.start >= other.start and self.start <= other.stop and self.stop >= other.start and self.stop <= other.stop:
                self.stop = other.stop
                self.start = other.start
                p.bugprint("# other is completely contained within me")
                return other
        # the other intersects my left
        elif other.stop >= self.start and other.stop <= self.stop:    
            self.start = other.start
            p.bugprint("# # the other intersects my left")
            return other
        # the other intersect my right
        elif other.start <= self.stop and other.start >= self.start:
            self.stop = other.stop
            p.bugprint(f"# the other intersect my right")
            return other

def solve(data):
    count = 0

    ranges = []

    for row in data:
        if not row: continue
        if "-" in row:
            start, stop = list(map(int, row.split("-")))
            new_range = Range(start, stop)             
            ranges.append(new_range)

     
    
    # go through each range

    repeat = True

    while repeat:
        repeat = False

        for this_range in ranges:

            for other_range in ranges:

                if this_range == other_range: continue

                to_delete = this_range.merge_and_get_deleted(other_range)

                if to_delete is not None:
                    repeat = True
                    break

            if to_delete is not None:
                break
        
        if to_delete is not None:
            ranges.remove(to_delete)
            p.bugprint("Ranges remaining: ", ranges)




    # and merge this range with any of the other ranges...

    

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

        
