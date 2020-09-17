feet = input("Enter your height in feet: ")
inch = input("Now enter your height in inches: ")
f = 12 #inches
i = 2.54 #cm
res = ((int(feet)*f)+int(inch))*i
print("Your height in metric system is: ", "%.2f" % res, "centimeters.")