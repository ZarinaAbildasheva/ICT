m = int(input())
n = [int(i) for i in input().split()]
count = 0
for i in range(m):
    for j in range(i+1, m):
        if n[i] == n[j]:
            count+=1
print(count)
