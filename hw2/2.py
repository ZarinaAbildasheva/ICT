a, a1 = [int(i) for i in input("Input the initial coordinates of the chess king: ").split()]
b, b1 = [int(i) for i in input("Input the final coordinates of the chess king: ").split()]
if(a>8 or a1>8 or b>8 or b1>8):
    print("Error")
else:
    if abs(a-b)<=1 and abs(a1-b1)<=1:
        print("YES")
    else : print("NO")  