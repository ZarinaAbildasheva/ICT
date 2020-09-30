n,m = [int(i) for i in input().split()]
a = [1]*n
for i in range(m):
    l,r = [int(j) for j in input().split()]
    for k in range(l-1, r):
        a[k] = 0
for h in range(n):
    if a[h] == 1:
        print("I", end = "")
    else:
        print(".", end = "")