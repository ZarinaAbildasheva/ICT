print("Please enter the cost of your meal: ", end="")
cost = float(input())
tax_p = 12
tip_p = 18
tax = (cost*tax_p)/100
tip = (cost*tip_p)/100
print("Calculated tax is: ",end="")
print("%.2f" % tax)
print("Calculated tip is: ", end = "")
print("%.2f" % tip)
gr = tax+tip+cost
print("Grand Total: ", end="")
print("%.2f" % gr)