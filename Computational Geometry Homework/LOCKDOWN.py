class QuickHull:
    def find(self, S):
        if len(S) <= 2:
            return []

        self.convex_hull = []
        top_right_point = S[0]
        bottom_left_point = S[0]

        for p in S:
            if p[0] > top_right_point[0]:
                top_right_point = p
            elif p[0] == top_right_point[0]:
                if p[1] > top_right_point[1]:
                    top_right_point = p

            if p[0] < bottom_left_point[0]:
                bottom_left_point = p
            elif p[0] == bottom_left_point[0]:
                if p[1] < bottom_left_point[1]:
                    bottom_left_point = p

        S1 = []
        S2 = []
        for p in S: 
            if (self.check_clockwise(bottom_left_point, top_right_point, p) < 0):
                S1.append(p)
            if (self.check_clockwise(top_right_point, bottom_left_point, p) < 0):
                S2.append(p)

        self.convex_hull.append(bottom_left_point)
        self.find_hull(S1, bottom_left_point, top_right_point)
        self.convex_hull.append(top_right_point)
        self.find_hull(S2, top_right_point, bottom_left_point)
    
        if len(self.convex_hull) == 2:
            self.convex_hull = []

        return self.convex_hull

    def square_distance(self, point, line):
        res = abs(self.check_clockwise(line[0], point, line[1]))**2 / self.square_length(line)
        return res

    def check_clockwise(self, p1, p2, p3):
        res = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
        return res

    def square_length(self, line):
        return (line[0][0] - line[1][0])**2 + (line[0][1] - line[1][1])**2


    def find_hull(self, Sk, P, Q):
        if (len(Sk) == 0): 
            return

        furthestPoint = Sk[0]
        max_sqr_dist = 0
        for p in Sk:
            sqr_dist = self.square_distance(p, [P, Q])
            if(sqr_dist > max_sqr_dist): 
                max_sqr_dist = sqr_dist
                furthestPoint = p
        

        S1 = []
        S2 = []
        for p in Sk: 
            if (self.check_clockwise(P, furthestPoint, p) < 0):
                S1.append(p)
            if (self.check_clockwise(furthestPoint, Q, p) < 0):
                S2.append(p)
        self.find_hull(S1, P, furthestPoint)
        self.convex_hull.append(furthestPoint)
        self.find_hull(S2, furthestPoint, Q)

class Solution:
    def get_input(self):
        self.S = []
        n = int(input())
        for i in range(n):
            x, y = map(int,input().strip().split(' '))
            self.S.append([x, y])

    def solve(self):
        self.get_input()
        self.S.sort()
        self.res = 0
        while True:
            convex_hull = QuickHull().find(self.S)
            if len(convex_hull) == 0:
                break


            self.res += 1

            convex_hull.sort()
            pos = 0
            temp = []
            for i in range(len(self.S)):
                if self.S[i] == convex_hull[pos]:
                    pos += 1
                else:
                    temp.append(self.S[i])
            self.S = temp

        print(self.res)

    def test(self):
        self.get_input()
        convex_hull = QuickHull().find(self.S)
        for p in convex_hull:
            print(p)
        


Solution().solve()
# Solution().test()