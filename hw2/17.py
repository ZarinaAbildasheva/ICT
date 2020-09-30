n = int(input())
count = 1
arr = [int(i) for i in input().split()]
for i in range(0,n-1):
    if arr[i] != arr[i+1]:
        count+=1
print(count)