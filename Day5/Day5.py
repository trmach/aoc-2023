import sys

# This was a great lesson in the importance of optimizing code.

# Naive implementation which the OS kills because it uses so much damn memory. 
# I learned the hard way.

# def f(map, d): # map[0] = dest, map[1] = source, map [2] = range length: Generates a mapping
#     for n in range(map[2]):
#         d[map[1] + n] = map[0] + n

# def g(d, x):
#     if x in d:
#         return d[x]
#     else:
#         return x

# def solve1(input):
#     maps = []
#     seeds = input[0][0]
#     for i in range(1, 8):
#         d = {}
#         for n in range(len(input[i])):
#             f(input[i][n], d) # function which mutates d
#         maps.append(d)

#     l = []
#     for seed in seeds:
#         l.append(g(maps[6], g(maps[5], g(maps[4], g(maps[3], g(maps[2], g(maps[1], g(maps[0], seed))))))))

#     return min(l)

def f(maps, n): # map[0] = dest, map[1] = source, map [2] = range length: Returns mapped value
    for map in maps:
        dest = map[0]
        source = map[1]
        range = map[2]

        if n >= source and n < source + range:
            return dest - source + n

    else: # n isn't in any of the ranges we explored
        return n


def solve1(input):
    seeds = input[0][0]
    l = float('inf')
    for seed in seeds:
        out = f(input[7], f(input[6], f(input[5], f(input[4], f(input[3], f(input[2], f(input[1], seed)))))))
        l = min(l, out)
    
    return l

# nice 15 python3 Day5.py input.txt 0 &
# nice 15 python3 Day5.py input.txt 4 &
# nice 15 python3 Day5.py input.txt 8 &
# nice 15 python3 Day5.py input.txt 12 &
# nice 15 python3 Day5.py input.txt 16 &
def solve2(input, a):
    seeds = []
    for n in range(a, a+4, 2):
        seeds.append((input[0][0][n], input[0][0][n+1]))
    l = float('inf')
    ranges = []
    for seed in seeds:
        for i in range(seed[0], seed[0] + seed[1]): # BRRRR
            for r in ranges:
                if i >= r[0] and i < r[0] + r[1]:
                    break # not good enough
                else:
                    out = f(input[7], f(input[6], f(input[5], f(input[4], f(input[3], f(input[2], f(input[1], i)))))))
                    if out < l:
                        l = out

        ranges.append(seed)
            
    return l

# ChatGPT (3.5):
# def solve2(input): # this is the funniest shit i've ever seen. after this it told me to memoize f
#     seeds = [(input[0][0][n], input[0][0][n+1]) for n in range(0, len(input[0][0]), 2)]
#     min_value = float('inf')
#     precomputed_values = [f(input[7], f(input[6], f(input[5], f(input[4], f(input[3], f(input[2], f(input[1], i))))))) for i in range(max(seeds, key=lambda x: x[0])[0] + max(seeds, key=lambda x: x[1])[1])]
#     ranges = set()
#     print("done")
#     for seed in seeds:
#         for i in range(seed[0], seed[0] + seed[1]):
#             if i in ranges:
#                 continue

#             current_value = precomputed_values[i]

#             if current_value < min_value:
#                 min_value = current_value

#             ranges.add(i)

#     return min_value

def main():
    if len(sys.argv) < 2:
        print("Exiting. No filepath specified")
        return
    else:
        with open(sys.argv[1], 'r') as file:
            #input = [x[:-1] for x in file.readlines()]
            input = [x.split(':')[1].strip().split('\n') for x in file.read().split('\n\n')]
            input = [[[int(i) for i in x.split()] for x in input[n]] for n in range(8)] # <3
            print(f"Part 1: {solve1(input)}")
            print(f"Part 2: {solve2(input, int(sys.argv[2]))}")

if __name__ == '__main__':
    main()