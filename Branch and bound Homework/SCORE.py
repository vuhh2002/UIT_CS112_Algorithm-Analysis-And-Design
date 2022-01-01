def solve(deg, cur, last):

  if deg >= k:
    if cur == s:
      return True
    else:
      return False

  for i in range(n):
    if last <= arr[i][deg] and arr[i][deg] * (k - deg) <= s - cur:
      if solve(deg + 1, cur + arr[i][deg], arr[i][deg]):            
        return True   

  return False

s, k, n = map(int, input().strip().split())
arr = [[int(x) for x in input().strip().split()] for i in range(n)]

if solve(0, 0, 0):
  print("YES") 
  
else:
  print("NO")