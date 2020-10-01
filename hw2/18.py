m = int(input())
n = [int(i) for i in input().split()]
first = n[m-1]
print(first, end = " ")
for j in range(0, m-1):
    print(n[j], end = " ")
