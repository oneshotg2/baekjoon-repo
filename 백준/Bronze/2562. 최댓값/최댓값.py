import sys
arr = [int(sys.stdin.readline()) for _ in range(9)]
maxval = max(arr)
print(maxval)
print(arr.index(maxval)+1)