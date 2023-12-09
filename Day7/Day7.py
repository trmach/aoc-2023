import sys


# use a frequency dictionary for each hand: {face: frequency}
# then if length 1 => five of a kind => set(5)
# if length 2 => four of a kind/full house => set(4, 1)/set(3, 2)
# if length 3 => three of a kind/two pair => set(3, 1)/set(2, 1)
# if length 4 => One pair => set(2, 1)
# if length 5 => High card => set(1)

map_ = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
mapJ = {'A':14, 'K':13, 'Q':12, 'J':1, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}

class Hand:
    def __init__(self, hand=''):
        self.hand = hand

    #* returns an integer corresponding to a hand's classification:
    #* High card       -> 0
    #* One pair        -> 1
    #* Two Pair        -> 2
    #* Three of a kind -> 3
    #* Full house      -> 4
    #* Four of a kind  -> 5
    #* Five of a kind  -> 6
    def classify(self):
        if len(set(self.hand)) == 5: # High Card
            return 0
        elif len(set(self.hand)) == 4: # One Pair
            return 1
        elif len(set(self.hand)) == 1: # Five of a kind
            return 6
        else:
            dself = {} # {label: frequency}
            for x in self.hand:
                if x not in dself: dself[x] = 1
                else: dself[x] += 1
            fs = sorted(dself.values())

            if fs == [1, 2, 2]: # Two pair
                return 2
            elif fs == [1, 1, 3]: # Three of a kind
                return 3
            elif fs == [2, 3]: # Full House
                return 4
            elif fs == [1, 4]: # Four of a kind
                return 5
    
    def __lt__(self, other): # x.__lt__(y) <=> x < y; x has a lower rank than y
        if self.classify() < other.classify():
            return True
        elif self.classify() > other.classify():
            return False
        else:
            for x, y in zip(self.hand, other.hand):
                if map_[x] == map_[y]:
                    continue
                else:
                    return map_[x] < map_[y]
    
        return False
    
    def __repr__(self):
        return repr(self.hand)

class HandJ:
    def __init__(self, hand=''):
        self.hand = hand

    def classify(self):
        if 'J' not in self.hand:
            return Hand(self.hand).classify()
        else:
            dself = {}
            for x in self.hand:
                if x != 'J':
                    if x not in dself: dself[x] = 1
                    else: dself[x] += 1
            max = ('0', 0)
            for k, v in dself.items(): # get most frequently occuring 
                if v > max[1]:
                    max = (k, v)
            return Hand(self.hand.replace('J', max[0])).classify()
            
    def __lt__(self, other): # x.__lt__(y) <=> x < y; x has a lower rank than y
        
        if self.classify() < other.classify():
            return True
        elif self.classify() > other.classify():
            return False
        else:
            for x, y in zip(self.hand, other.hand):
                if mapJ[x] == mapJ[y]:
                    continue
                else:
                    return mapJ[x] < mapJ[y]
    
        return False
    
    def __repr__(self):
        return repr(self.hand)

# ***This is a Min Heap*** #
class Heap: # thanks to Prof. Lee for teaching me DS and providing valuable resources
    def __init__(self):
        self.data = []

    @staticmethod
    def left(i):
        return 2*i + 1
    
    @staticmethod
    def right(i):
        return 2*i + 2
    
    @staticmethod
    def parent(i):
        return (i - 1) // 2
    
    def add(self, x):
        self.data.append(x)
        idx = len(self.data) - 1
        while idx > 0:
            pidx = Heap.parent(idx)
            if self.data[idx][0] < self.data[pidx][0]: #* Min Heap
                self.data[idx], self.data[pidx] = self.data[pidx], self.data[idx]
                idx = pidx
            else:
                break
    
    def heapify(self, idx = 0):
        while idx < len(self.data):
            lidx = Heap.left(idx)
            ridx = Heap.right(idx)
            mxidx = idx
            if lidx < len(self.data) and self.data[lidx][0] < self.data[mxidx][0]: # Should be using a lambda
                mxidx = lidx
            if ridx < len(self.data) and self.data[ridx][0] < self.data[mxidx][0]:
                mxidx = ridx
            if mxidx != idx:
                self.data[idx], self.data[mxidx] = self.data[mxidx], self.data[idx]
                idx = mxidx
            else:
                break
    
    def pop(self):
        assert len(self) > 0
        ret = self.data[0]
        self.data[0] = self.data[-1]
        del self.data[-1]
        self.heapify()
        return ret
    
    def min(self):
        assert len(self) > 0
        return self.data[0]

    def __len__(self):
        return len(self.data)
    
    def __bool__(self):
        return len(self.data) > 0
    

def solve1(input):
    h = Heap()
    hands = [(Hand(x[0]), int(x[1])) for x in [y.split() for y in input]]

    for hand in hands:
        h.add(hand)
    
    l = []
    while h:
        l.append(h.pop())
    total = 0
    for x, y in enumerate(l):
        total += (x+1)*y[1]

    return total

def solve2(input):
    h = Heap()
    hands = [(HandJ(x[0]), int(x[1])) for x in [y.split() for y in input]]

    for hand in hands:
        h.add(hand)
    
    l = []
    while h:
        l.append(h.pop())
    total = 0
    for x, y in enumerate(l):
        total += (x+1)*y[1]

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