n = int(input())
max = 0
cnt = 0
while(n != 0):
    if n>max:
        max = n
        cnt = 0
    if max == n:
        cnt+=1
    n = int(input())
print(cnt)