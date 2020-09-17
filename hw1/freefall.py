height = float(input("Enter the height from which object is dropped(m): "))
g = 9.8
res = (2*g*height)**(1/2)
print("Final velocity of the object when it hits the ground %.2f" % res)