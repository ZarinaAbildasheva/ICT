s = float(input("Enter the length of polygon side: "))
n = int(input("Enter amount of the polygon's sides: "))
import math
tangent = math.tan(math.pi/n)
area = (n*(s**2))/4*tangent
print("Area of the polygon equals to ", area)