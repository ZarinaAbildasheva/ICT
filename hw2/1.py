a, a1 = [int(i) for i in input("Input the initial place of the chess rook: ").split()]
b, b1 = [int(i) for i in input("Input the final place of the chess rook: ").split()]
if(a>8 or a1>8 or b>8 or b1>8):
    print("Error")
else:
    if a==b or a1==b1:
        print("YES")
    else : print("NO")   