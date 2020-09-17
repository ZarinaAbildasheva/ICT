p = float(input("Enter the pressure: "))
v = float(input("Enter the volume of the gas: "))
t = float(input("Enter the temperature: "))
r = 8.314
tem = t+273.15
n = (p*v)/(r*tem)
print("Amount of gas in moles equals to %.2f moles." %n)