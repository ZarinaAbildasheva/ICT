a, a1 = [int(i) for i in input("Input the initial coordinates of the chess horse: ").split()]
b, b1 = [int(i) for i in input("Input the final coordinates of the chess horse: ").split()]
if(a>8 or a1>8 or b>8 or b1>8):
    print("Error")
else:
    c = abs(a-a1)
    d = abs(b-b1)
    if c == 1 and d == 2 or c == 2 and d == 1:
        print("YES")
    else : print("NO")  