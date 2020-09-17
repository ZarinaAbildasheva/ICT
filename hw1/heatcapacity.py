massa = float(input("Enter the mass of the water in milligrams: "))
#m=pv then v = m especially for water
t = float(input("Enter the change of the Temperature: "))
specific_heat = 4.186
density = 1
el_kwh = 8.9
q = specific_heat*massa*t
print("Total amount of energy: ", q, " Joules")
kwh = el_kwh*(q/(3.6*1000000))
print("Electricity costs: %.2f" % kwh, "dollars")