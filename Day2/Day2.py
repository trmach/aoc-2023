import sys

def solve1(input):
    colormap = {"red":0, "green":1, "blue":2}
    games = 0
    for s in range(len(input)):
        game = input[s].split(':')
        gamenumber = int(game[0].split()[1])
        hands = game[1].split(';')
        possible = True
        for hand in hands:
            rgb = [0, 0, 0]
            for cubes in hand.split(','):
                tokens = cubes[1:].split()
                rgb[colormap[tokens[1]]] += int(tokens[0]) # ghc is shaking
            if not all([rgb[0] <= 12, rgb[1] <= 13, rgb[2] <= 14]):
                possible = False
        if possible:
            games += gamenumber
                    

    return games

def solve2(input):
    colormap = {"red":0, "green":1, "blue":2}


def main():
    if len(sys.argv) < 2:
        print("Exiting. No filepath specified")
        return
    else:
        with open(sys.argv[1], 'r') as file:
            input = [x[:-1] for x in file.readlines()] # much cleaner
            print(solve1(input))

if __name__ == '__main__':
    main()