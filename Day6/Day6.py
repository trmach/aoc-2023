import sys

def solve1(input):
    ts = input[0].split(':')[1].strip().split()
    ds = input[1].split(':')[1].strip().split()
    races = [(int(ts[n]), int(ds[n])) for n in range(len(ts))]
    total = 1
    for race in races: #* (Time, Record)
        wins = 0
        #* we need to check each possibility from 1 to length_of_race-1 with a quadratic equation
        #* if we hold button for t seconds, it will travel at t*seconds^2 for length_of_race-t seconds
        for t in range(1, race[0]):
            if (race[0] - t)*t > race[1]: #* <- Quadratic
                wins += 1
        total *= wins

    return total
    

def solve2(input):
    ts = int(input[0].split(':')[1].replace(' ', ''))
    ds = int(input[1].split(':')[1].replace(' ', ''))
    total = 1
    wins = 0
    for t in range(1, ts):
        if (ts - t)*t > ds:
            wins += 1
    total *= wins

    return total

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