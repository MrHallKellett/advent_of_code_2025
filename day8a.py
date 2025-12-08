from re import search, match, findall
from collections import Counter, defaultdict
from itertools import product, combinations, permutations
from math import inf as INF
from math import prod, sqrt
from helpers import *

PP_ARGS = False, False #rotate, cast int

DAY = 8
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689///40
"""

DEBUG = False


distance_map = {}

def calculate_distance(a, b):
    return sqrt(abs(a.x - b.x)**2 + abs(a.y - b.y)**2 + abs(a.z - b.z)**2)

class Junction:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"{self.x} {self.y} {self.z}"

    def get_distance(self, oj):

        return distance_map[self][oj]
    
        
    
class Circuit:
    def __init__(self, j : Junction):
        self.junctions = [j]

    def __repr__(self):
        return f"{self.junctions}"

    def __contains__(self, item):
        return item in self.junctions
    
    def get_distance(self, other_circuit):
        # dodgy
        if any(j in self for j in other_circuit.junctions):
            return INF
        
        smallest = INF
        for j1 in self.junctions:
            for j2 in other_circuit.junctions:
                distance = j1.get_distance(j2)
                if distance < smallest:
                    smallest = distance
        return smallest
    
    def join(self, other_circuit):
        self.junctions.extend(other_circuit.junctions)

    def get_size(self):
        return len(self.junctions)

desired_conns = 10

def solve(data):
    count = 0
    
    circuits = []
    global distance_map

        
    for row in data:
        x,y,z = list(map(int, row.split(",")))
        j = Junction(x, y, z)
        
        distance_map[j] = {}
        

        for key in distance_map.keys():
            if key == j:    continue
            distance = calculate_distance(key, j)
            try:
                distance_map[key][j] = distance
            except:
                distance_map[key] = {j:distance}
            

        circuits.append(Circuit(j))

    
    

    connections_made = 0
    while connections_made < desired_conns - 1:
        smallest = INF
        for c1 in circuits:
            for c2 in circuits:
                if c1 == c2:    continue
                distance = c1.get_distance(c2)
                p.bugprint(f" distance between {c1} and {c2} is {distance}")
                if distance < smallest:
                    smallest = distance
                    best = (c1, c2)
        
        c1, c2 = best
        p.bugprint(f"Best to join {c1} and {c2}")
        p.bugprint()
        
        # merge
        c1.join(c2)
        circuits.remove(c2)
        connections_made += 1
        p.bugprint("current circuits")
        p.bugprint(circuits)
        p.buginput()


    for i, circuit in enumerate(circuits):
        print(i, circuit)


    top_3 = sorted(circuit.get_size() for circuit in circuits)[-3:]

    print(top_3)

    return prod(top_3)


    




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    try:
        if p.check(TESTS, solve):
            desired_conns = 1000
            puzzle_input = p.load_puzzle()
            puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
            print("FINAL ANSWER: ", solve(puzzle_input))
    except Exception as e:
        p.log.close()
        raise e

        
