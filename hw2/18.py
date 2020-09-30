n = [int(i) for i in input().split()]
first = n[len(n)-1]
print(first, end = " ")
for j in range(0, len(n)-1):
    print(n[j], end = " ")