def partitionAsc(arr, low, high):
  i = (low-1)	
  pivot = arr[high]	

  for j in range(low, high):
    if arr[j] <= pivot:
			  i = i+1
			  arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return (i+1)


def quickSortAsc(arr, low, high):
	if len(arr) == 1:
		return arr

	if low < high:
		pi = partitionAsc(arr, low, high)
		quickSortAsc(arr, low, pi-1)
		quickSortAsc(arr, pi+1, high)


def partitionDes(arr, low, high):
  i = (low-1)	
  pivot = arr[high]	

  for j in range(low, high):
    if arr[j] >= pivot:
			  i = i+1
			  arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return (i+1)


def quickSortDes(arr, low, high):
	if len(arr) == 1:
		return arr

	if low < high:
		pi = partitionDes(arr, low, high)
		quickSortDes(arr, low, pi-1)
		quickSortDes(arr, pi+1, high)


n, m = map(int, input().split())
arr = list(map(int,input().strip().split()))[:n]
if m:
  quickSortDes(arr, 0, n-1)
else:
  quickSortAsc(arr, 0, n-1)
print(*arr)
