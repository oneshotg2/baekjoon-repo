import sys
import math
arr_length, tryit = map(int,sys.stdin.readline().split())
arr_count = [i for i in range(1,arr_length+1)]
for _ in range(tryit):
    x,y = map(int,sys.stdin.readline().split())
    if x != y:
        for i in range(math.ceil((y-x)/2)):
            arr_count[x-1+i], arr_count[y-1-i] = arr_count[y-1-i], arr_count[x-1+i]

for i in arr_count:
    print(i, end=" ")