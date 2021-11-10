import random
import string
from solution import Solution

class Testing:
    def __init__(self):
        self.board = None
        self.word = None

        self.output = None
        self.extraInfo = None
        self.order = None

        self.letters = []
        self.m = None
        self.n = None

    def letterAt(self, pos):
        return self.board[pos[0]][pos[1]]

    def getWordLength(self):
        return random.randint(1, min(15, self.m * self.n))

    def randBoard(self, isMaxSize=False):
        if isMaxSize:
            self.n = 6
            self.m = 6
        else:
            self.n = random.randint(1,6)
            self.m = random.randint(1,6)

        self.randLetterList()

        self.board = []
        for i in range(self.m):
            row = []
            for j in range(self.n):
                row.append(random.choice(self.letters))

            self.board.append(row)

    def randLetterList(self):
        numOfLetter = random.randint(2, max(self.m * self.n * 2 // 5 - 2, 2))
        self.letters = [random.choice(string.ascii_letters)]

        while len(self.letters) < numOfLetter:
            letter = random.choice(string.ascii_letters)
            while letter in self.letters:
                letter = random.choice(string.ascii_letters)
            self.letters.append(letter)

    def randRightWord(self):
        path = [[random.randint(0,self.m-1), random.randint(0,self.n-1)]]
        self.word = self.letterAt(path[-1])

        wordLength = self.getWordLength()

        while len(path) < wordLength:
            nextPosList = [
                [path[-1][0] + 1, path[-1][1]],
                [path[-1][0] - 1, path[-1][1]],
                [path[-1][0], path[-1][1] + 1],
                [path[-1][0], path[-1][1] - 1],
            ]
            for a in nextPosList.copy():
                if a in path or a[0] < 0 or a[0] >= self.m or a[1] < 0 or a[1] >= self.n:
                    nextPosList.remove(a)
            if len(nextPosList) == 0:
                break
            path.append(random.choice(nextPosList))
            self.word += self.letterAt(path[-1])

    def randWord(self):
        wordLength = self.getWordLength()
        self.word = ""
        for i in range(wordLength):
            self.word += random.choice(self.letters)

    def makeRightCase(self):
        self.randBoard()
        self.randRightWord()
        self.output = "true"

    def makeWrongCase(self):
        self.randBoard()
        self.output = "true"
        count = 0
        while self.output == "true":
            if count == 10:
                self.randBoard()
                count = 0
            self.randWord()
            self.solve()
            count += 1

    def solve(self):
        solution = Solution()
        self.output = solution.solve(self.board, self.word)
        self.extraInfo = solution.getExtraInfo()

    def getInput(self) -> str:
        return str(self.board) + "\n" + str(self.word)

    def toFile(self, input: str, output, extraInfo):
        i = open("in\input" + str(self.order) + ".txt", 'w')
        i.write(input)
        i.close()

        o = open("out\output" + str(self.order) + ".txt", 'w')
        o.write(str(output))
        o.close()

        e = open("extraInfo\extraInfo" + str(self.order) + ".txt", 'w')
        e.write(str(extraInfo))
        e.close()

        self.order += 1

    def generateTestSet(self, makeCase, firstOrder, lastOrder):
        self.order = firstOrder
        n = lastOrder - firstOrder + 1
        for i in range(n):
            makeCase()
            self.toFile(self.getInput(), self.output, self.extraInfo)

    def checkCase(self, order):
        i = open("in\input" + str(order) + ".txt", 'r')
        print(i.read())
        i.close()

        o = open("out\output" + str(order) + ".txt", 'r')
        print(o.read())
        o.close()
        
        e = open("extraInfo\extraInfo" + str(order) + ".txt", 'r')
        print(e.read())
        e.close()

    def checkRange(self, i, j):
        for order in range(j, i-1, -1):
            print("\nCase", order)
            self.checkCase(order)

testing = Testing()

# testing.generateTestSet(testing.makeWrongCase, 1,50)
# testing.generateTestSet(testing.makeRightCase, 51,100)

# testing.checkRange(51,55)
# testing.checkRange(1,5)