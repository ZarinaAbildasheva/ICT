price = 3.49
p = 60
n = int(input("Enter amount of bread loaves: "))
ordinary = round((price*n),2)
sale = round(((ordinary*60)/100), 2)
discount = round((ordinary-sale), 2)
print("Ordinary price:", ordinary)
print("Sale:", sale)
print("Discount:", discount)