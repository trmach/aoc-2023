import sys

def solve1(cards):
    sum = 0
    for card in cards:
        s = set()
        c = [x.strip().split() for x in card.split(':')[1].split('|')]
        winnings = c[0]
        have = c[1]
        for win in winnings:
            if win in have:
                s.add(win)
        if len(s) >= 1:
            sum += 2**(len(s) - 1)
    return sum

def playall(wins):
    pass
        
def solve2(cards):
    numberOfWins = {}
    for card in cards:
        s = set()
        cardnumber = int(card.split(':')[0].split()[1])
        c = [x.strip().split() for x in card.split(':')[1].split('|')]
        winnings = c[0]
        have = c[1]

        for win in winnings:
            if win in have:
                s.add(win) # we need s JUST to represent the number of wins for a card

        numberOfWins[cardnumber] = len(s)
    
    l = [[k, 1] for k, v in numberOfWins.items()] # this was the worst ever
    for i in range(len(l)):
        for n in range(i+1, i+1+numberOfWins[l[i][0]]):
            l[n][1] += l[i][1]

    print(l)
    return sum([n[1] for n in l])


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