import sys
arr_boolean = [False] * 42
for _ in range(10):
    num = int(input())%42
    arr_boolean[num] = True
print(arr_boolean.count(True))