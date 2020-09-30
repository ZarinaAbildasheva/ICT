n = int(input())
a = 0
b = 1
cnt = 0
while(b<=n):
    cnt+=1
    a,b = b, a+b
if a == n:
    print(cnt)
else: 
    print(-1)