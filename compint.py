saving = input("Enter your amount of money: ")
p = 4
first_year = (((int(saving)*4)/100)+int(saving))
second_year = ((first_year*4)/100)+first_year
third_year = ((second_year*4)/100)+second_year
print("Amount of money after 1 year: " + str("%.2f" % first_year))
print("Amount of money after 2 years: " + str("%.2f" % second_year))
print("Amount of money after 3 years: " + str("%.2f" % third_year))