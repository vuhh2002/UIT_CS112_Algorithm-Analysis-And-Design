# https://www.spoj.com/PTIT/submit/BCTSP/
class Solution:		
	def solve(self):
		self.get_input()
		self.min_cost = float('inf')
		self.visited = [False] * self.n
		self.visited[0] = True
		self.count = 1
		self.cost = 0
		self.search(0)
		print(self.min_cost)

	def get_input(self):
		self.n = int(input().strip())
		self.C = []
		for i in range(self.n):
			self.C.append(list(map(int,input().strip().split())))

	def lower_bound(self, current_pos):
		if current_pos == 0 or self.count == self.n:
			return -1
		res = self.cost

		cities = set()
		cities.add(current_pos)
		cities.add(0)
		for i in range(self.n):
			if not self.visited[i]:
				cities.add(i)

		cities = list(cities)
		min_line_cost = 10000
		for a in cities:
			for b in cities:
				if self.C[a][b] != 0:
					min_line_cost = min(min_line_cost, self.C[a][b])

		res += min_line_cost * (self.n - self.count + 1)
		return res

	def search(self, current_pos):
		if self.lower_bound(current_pos) >= self.min_cost:
			return

		if self.count == self.n and self.C[current_pos][0]:
			self.min_cost = min(self.min_cost, self.cost + self.C[current_pos][0])
			return

		for i in range(self.n):
			if not self.visited[i] and self.C[current_pos][i]:
				self.cost += self.C[current_pos][i]
				self.count += 1
				self.visited[i] = True
				
				self.search(i)

				self.cost -= self.C[current_pos][i]
				self.count -= 1
				self.visited[i] = False

Solution().solve()