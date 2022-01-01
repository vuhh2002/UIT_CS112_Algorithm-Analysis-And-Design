import random
from solution import Solution

class Testing:
    def __init__(self):
        self.order = None
        self.output = None
        self.extraInfo = None

        self.n = None
        self.num = None

    def addNumber(self, number):
        self.extraInfo.append(number)
        temp = str(number)
        self.num += temp
        self.n += len(temp)

    def makeRightCase(self):
        self.output = "true"
        self.extraInfo = []
        self.num = ""
        self.n = 0
        m = random.randint(3,35)
        
        for i in range(2):
            number = random.randint(0, m // 3)
            self.addNumber(number)

        number = self.extraInfo[-1] + self.extraInfo[-2]
        while self.n + len(str(number)) <= m:
            self.addNumber(number) 
            number = self.extraInfo[-1] + self.extraInfo[-2]

    def makeWrongCase(self):
        self.n = random.randint(1,35)
        self.output = "true"
        while self.output == "true":
            self.num = ""
            for i in range(self.n):
                self.num += str(random.randint(0,9))
            self.solve()
            
    def toWrongCase(self):
        if self.output != "true":
            self.makeRightCase()

        extraInfo = self.extraInfo

        while self.output == "true":
            index = random.randint(0, len(self.num) - 1)
            temp = int(self.num[index]) + random.randint(1,9)
            self.num = self.num[:index] + str(temp % 10) + self.num[index+1:]

            self.solve()

        self.extraInfo = extraInfo

    def solve(self):
        solution = Solution()
        self.output = solution.solve(self.num)
        self.extraInfo = solution.getExtraInfo()

    def getInput(self):
        return str(self.num)

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

# testing.generateTestSet(testing.toWrongCase, 1,25)
# testing.generateTestSet(testing.makeWrongCase, 26,50)
# testing.generateTestSet(testing.makeRightCase, 51,100)

# testing.checkRange(51,55)
# testing.checkRange(26,30)
# testing.checkRange(1,5)