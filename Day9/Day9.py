import sys

def solve1(input):
    acc = 0
    for seq in input:
        diff = 0
        a = []
        n = [int(x) for x in seq.split()]
        a.append(n)
        while not all(x == 0 for x in n):
            diffs = []
            for i in range(1, len(n)):
                diff = n[i] - n[i-1]
                diffs.append(diff)
            n = diffs
            a.append(diffs)  

        a.reverse()
        for l in enumerate(a):
            i, lst = l[0], l[1]
            if i == 0:
                lst.append(0)
                continue
            a[i].append(a[i - 1][-1] + lst[-1])
        
        acc += a[-1][-1]

    return acc;

def solve2(input):
    acc = 0
    for seq in input:
        diff = 0
        a = []
        n = [int(x) for x in seq.split()]
        a.append(n)
        while not all(x == 0 for x in n):
            diffs = []
            for i in range(1, len(n)):
                diff = n[i] - n[i-1]
                diffs.append(diff)
            n = diffs
            a.append(diffs)  

        a.reverse()
        for l in a:
            l.reverse()
        for l in enumerate(a):
            print(l)
            i, lst = l[0], l[1]
            if i == 0:
                lst.append(0)
                continue
            a[i].append(lst[-1] - a[i - 1][-1])
        
        acc += a[-1][-1]

    return acc;

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
