n,m=map(int, input().strip().split())
diff = [set() for i in range(n+m)]
fake = n
all = set()
for i in range(m):
    i,j,c = input().strip().split()
    i,j =int(i)-1,int(j)-1
    all.add(i)
    all.add(j)
    if c == "1":
        diff[i].add(fake)
        diff[j].add(fake)
        diff[fake].add(i)
        diff[fake].add(j)
        fake += 1
    else:
        diff[i].add(j)
        diff[j].add(i)

all = list(all)
team_code = [-1] * (n+m)

def bfs(i):
    queue = [i]
    while len(queue) > 0:
        i = queue.pop(-1)
        for j in diff[i]:
            if team_code[j] == -1:
                team_code[j] = team_code[i] ^ 1
                queue.append(j)
            elif team_code[j] == team_code[i]:
                print("YES")
                exit(0)

for i in all:
    if team_code[i] == -1:
        team_code[i] = 0
        bfs(i)

print("NO")