import sys

def getAdjacent(i, j): # the input *conveniently* does not put symbols at the top or bottom rows or at the ends of lines
    l = []
    for y in range(j-1, j+2):
        for x in range(i-1, i+2):
            if x != i or y != j: # we know we don't want the center cell (the one we started with)
                l.append((x, y))
    return l

def extract(input, i): # the symbol at i is a digit and we want to find its start and end
    upper = lower = i
    try: # suck it up
        while(input[upper+1].isdigit()):
            upper += 1
    except IndexError:
        pass
    try:
        while(input[lower-1].isdigit()):
            lower -= 1
    except IndexError:
        pass
    return input[lower:upper+1]

def merge(l):
    m = {}
    for x, y in l:
        if y in m:
            m[y].append(x)
        else:
            m[y] = [x]
    return m

def solve1(input):
    width = len(input[0])
    height = len(input)
    s = set('~!@#$%^&*()_+{}|:"<>?`-=\;,/')
    sum = 0

    for j in range(height):
        for i in range(width):
            if input[j][i] in s:
                l = getAdjacent(i, j)
                nums = set()
                for x, y in l:
                    if input[y][x].isdigit():
                        nums.add(int(extract(input[y], x)))
                for n in nums:
                    sum += n

    return sum

def solve2(input): # ez
    width = len(input[0])
    height = len(input)
    sum = 0

    for j in range(height):
        for i in range(width):
            if input[j][i] == '*':
                l = getAdjacent(i, j)
                nums = set()
                for x, y in l:
                    if input[y][x].isdigit():
                        nums.add(int(extract(input[y], x)))
                if len(nums) == 2:
                    one = 1
                    for n in nums:
                        one *= n
                    sum += one

    return sum

def main():
    if len(sys.argv) < 2:
        print("Exiting. No filepath specified")
        return
    else:
        with open(sys.argv[1], 'r') as file:
            input = [x[:-1] for x in file.readlines()]
            print(f"Part 1: {solve1(input)}")
            print(f"Part 2: {solve2(input)}")

if __name__ == '__main__':
    main()