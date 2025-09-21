import sys
arr_size_count_max = list(map(int, sys.stdin.readline().split()))
count_list = [0 for _ in range(arr_size_count_max[0])]
for _ in range(arr_size_count_max[1]):
    x,y,z = map(int, sys.stdin.readline().split())
    for i in range(x,y+1):
        count_list[i-1] = z
    if(x==y): count_list[x-1] = z
for i in count_list:
    print(i, end=" ")