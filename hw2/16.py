n = int(input())
m = int(input())
next = 1
cnt = 0
while(next != 0):
    next = int(input())
    if m>next and m>n:
        cnt += 1
    n,m = m, next
print(cnt)