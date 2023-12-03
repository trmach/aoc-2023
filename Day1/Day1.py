import sys

def solve1(input):
    n = 0
    for line in input:
        for i in line:
            if i.isdigit():
                n += int(i)*10
                break
        for i in line[::-1]:
            if i.isdigit():
                n += int(i)
                break

    return n

def solve2(input):
    n = 0
    s = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    hit = False
    for line in input:
        hit = False
        i = 0
        while not hit and i < len(line):
            for j in range(i, i+6):
                if line[i].isdigit():
                    n += int(line[i])*10
                    hit = True
                    break
                elif line[i:j] in s.keys():
                    n += int(s[line[i:j]])*10
                    hit = True
                    break
            i += 1

        hit = False
        i = len(line)
        while not hit and i >= 0:
            for j in range(i, min(i+6, len(line))):
                if line[i].isdigit():
                    n += int(line[i])
                    hit = True
                    break
                elif line[i:j+1] in s.keys():
                    n += int(s[line[i:j+1]])
                    hit = True
                    break
            i -= 1

    return n

def parse(filepath):
    try:
        file = open(filepath, "r")
    except:
        raise Exception("File not found")
    return [x[:-1] for x in file.readlines()]

def main():
    if len(sys.argv) < 2:
        print("Exiting. No filepath specified")
        return
    else:
        input = parse(sys.argv[1])

    print(solve2(input))

if __name__ == '__main__':
    main()