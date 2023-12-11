import sys
import numpy as np

def solve1(input):
    dirs = input[0]
    d = {}
    for map in input[2:]:
        children = map.split('=')[1].strip().split(',')
        d[map.split('=')[0].strip()] = (children[0][1:].strip(), children[1][:-1].strip())
    
    node = 'AAA'
    count = 0
    dircount = 0
    while node != 'ZZZ':
        if dircount % len(dirs) == 0:
            dircount = 0

        if dirs[dircount] == 'L':
            node = d[node][0]
        elif dirs[dircount] == 'R':
            node = d[node][1]

        count += 1
        dircount += 1

    return count


def solve2(input): # *** All nodes which CONTAIN 'A' also END with 'A' ***
    dirs = input[0]
    d = {}
    for map in input[2:]:
        children = map.split('=')[1].strip().split(',')
        d[map.split('=')[0].strip()] = (children[0][1:].strip(), children[1][:-1].strip())
    
    nodes = [] # all nodes we follow
    counts = []
    dircount = 0
    n = 0

    for k in d.keys():
        if k[2] == 'A':
            nodes.append(k)
            counts.append(0)
    
    for node in nodes:
        while node[2] != 'Z':
            if dircount % len(dirs) == 0:
                dircount = 0
            
            if dirs[dircount] == 'L':
                node = d[node][0]
                counts[n] += 1

            elif dirs[dircount] == 'R':
                node = d[node][1]
                counts[n] += 1

            dircount += 1

        n += 1
    
    return np.lcm.reduce(counts) # Fake Programmer

def main():
    if len(sys.argv) < 2:
        print("Exiting. No filepath specified")
        return
    else:
        with open(sys.argv[1], 'r') as file:
            input = [x[:-1] for x in file.readlines()]
            print(f"Part 1: {solve1(input)}\nPart 2: {solve2(input)}")

if __name__ == '__main__':
    main()