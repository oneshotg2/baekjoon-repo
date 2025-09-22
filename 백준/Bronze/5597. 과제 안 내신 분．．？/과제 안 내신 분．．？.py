import sys
arr_boolean = [False] * 30
for _ in range(28):
    num = int(sys.stdin.readline())-1
    arr_boolean[num] = True
for i in range(30):
    if arr_boolean[i] == False: print(i+1)