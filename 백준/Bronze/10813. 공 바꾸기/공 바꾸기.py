import sys
arr_len, try_count = map(int, sys.stdin.readline().split())

count_list = [i+1 for i in range(arr_len)]
for _ in range(try_count):
    x,y = map(int, sys.stdin.readline().split())
    count_list[x-1], count_list[y-1] = count_list[y-1], count_list[x-1]
        

for i in count_list:
    print(i, end=" ")