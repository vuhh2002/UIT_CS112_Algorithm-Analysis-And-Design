# https://leetcode.com/problems/additive-number/
class Solution:
    def __init__(self):
        self.length = None
        self.additiveSequence = []
        self.num = None
    
    def isAdditiveNumber(self, num):
        self.length = len(num)
        self.num = num
        for i in range(1, self.length + 1):
            if self.search(i, num[:i]):
                return True
        return False
        
    def search(self, pos, stringNum):
        if len(stringNum) >= 2 and stringNum[0] == "0" \
        or (len(self.additiveSequence) >= 2 and self.additiveSequence[-2] + self.additiveSequence[-1] != int(stringNum)):
            return False
        
        if pos == self.length:
            if len(self.additiveSequence) <= 1:
                return False
            return True
        self.additiveSequence.append(int(stringNum))
        
        for i in range(pos + 1, self.length + 1):
            if self.search(i, self.num[pos:i]):
                return True
            
        self.additiveSequence.pop()
        return False

    def solve(self, num):
        if self.isAdditiveNumber(num):
            return "true"
        else:
            return "false"
    
    def getExtraInfo(self):
        return self.additiveSequence


num = input()
if Solution().isAdditiveNumber(num):
    print("true")
else:
    print("false")