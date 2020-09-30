a, a1 = [int(i) for i in input("Input the initial coordinates of the chess elefant: ").split()]
b, b1 = [int(i) for i in input("Input the final coordinates of the chess elefant: ").split()]
if(a>8 or a1>8 or b>8 or b1>8):
    print("Error")
else:
    if abs(a-b)==abs(b1-a1):
        print("YES")
    else: print("NO")  