n = int(input())
m = int(input())
x = int(input())
y = int(input())
maxi = max(n, m)
mini = min(n, m)
if x >= mini/2:
    x = mini - x
if y >= maxi/2:
    y = maxi - y
if x>y:
    print(y)
else:
    print(x) 