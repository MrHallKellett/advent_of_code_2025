from re import search, match, findall
from collections import Counter, defaultdict
from itertools import product, combinations, permutations
from math import inf as INF
from math import prod
from helpers import *


actual = '''.......S.......
.......|.......
......|^|......
......|.|......
.....|^|^|.....
.....|.|.|.....
....|^|^|^|....
....|.|.|.|....
...|^|^|||^|...
...|.|.|||.|...
..|^|^|||^|^|..
..|.|.|||.|.|..
.|^|||^||.||^|.
.|.|||.||.||.|.
|^|^|^|^|^|||^|
|.|.|.|.|.|||.|'''


expected = '''.......S.......
.......|.......
......|^|......
......|.|......
.....|^|^|.....
.....|.|.|.....
....|^|^|^|....
....|.|.|.|....
...|^|^|||^|...
...|.|.|||.|...
..|^|^|||^|^|..
..|.|.|||.|.|..
.|^|||^||.||^|.
.|.|||.||.||.|.
|^|^|^|^|^|||^|
|.|.|.|.|.|||.|'''





PP_ARGS = False, False #rotate, cast int

DAY = 7
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............///21
"""

DEBUG = True

SPLITTER = "^"

splitters = set()

beam_locs = set()

beams = set()

def beam(grid, x, y):
    beam_locs.add((x, y))
    
    y += 1
    try:
        new = grid[y][x]
    except IndexError:
        return
    if new == SPLITTER:
        if (x, y) not in splitters:
        
    
            beam(grid, x+1, y)
        
            if x > 0:
                beam(grid, x-1, y)
            
            splitters.add((x, y))
        else:
            print(f"Duplicate beam found at {x} {y}")
    else:
        beam(grid, x, y)
        

def display(data):
    s = ""
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if (x, y) in beam_locs:
                char = "|"
            else:
                char = data[y][x]
            s += char
        s += "\n"

    print(s)
    input()


def solve(data):
    global splitters, beam_locs
    splitters = set()

    beam_locs = set()


    count = 0

    start_x = data[0].index("S")

    beam(data, start_x, 0)
    display(data)
    return len(splitters)
        

        
    

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

        
