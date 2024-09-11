import sys

def solve1(input):
    # First, find S
    current = (0, 0)
    for j, elem in enumerate(input):
        try:
            current = (elem.index("S"), j) # find start position
            break
        except:
            continue



    print(current)

# | is a vertical pipe connecting north and south
# - is a horizontal pipe connecting east and west
# L is a 90-degree bend connecting north and east
# J is a 90-degree bend connecting north and west
# 7 is a 90-degree bend connecting south and west
# F is a 90-degree bend connecting south and east
# . is ground; there is no pipe in this tile
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has



def solve2(input):
    pass

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
