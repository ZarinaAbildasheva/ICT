a=int(input())
b=int(input())
c=int(input())
a1=int(input())
b1=int(input())
c1=int(input())
v = a*b*c
v1 = a1*b1*c1
summ = a+b+c
summ1 = a1+b1+c1
mini = min(a, b, c)
mini1 = min(a1, b1, c1)
maxi = max(a, b, c)
maxi1 = max(a1, b1, c1)
d = summ-mini-maxi
d1 = summ1-mini1-maxi1 
if v == v1 and (mini == mini1) and (maxi == maxi1) and d == d1:
    print("Boxes are equal")
elif v>=v1 and ((mini>=mini1) and (maxi>=maxi1)) and d >= d1:
    print("The first box is larger than the second one")
elif v<=v1 and ((mini1>=mini) and (maxi1>=maxi)) and d <= d1:
    print("The first box is smaller than the second one")
else:
    print("Boxes are incomparable")