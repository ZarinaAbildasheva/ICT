print("In this program we will calculate the area of the fermer's field")
print("Enter the length in feet: ", end="")
length = int(input())
print("Enter the width in feet: ", end="")
width = int(input())
area = length*width
areain_acre = area/43560
print("The area of the field is: "+str(areain_acre)+" acres")