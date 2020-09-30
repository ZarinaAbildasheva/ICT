n = int(input())

for i in range(1,int(n/2),1):
    if(i**2 <= n):
        print(i**2, end = " ")
    else:
        break