m = int(input())
twodollars = 200
onedollar = 100
quarter = 25
dime = 10
nickel = 5
print(str(m//twodollars) + " two dollars")
m %= twodollars
print(str(m//onedollar) + " one dollars")
m %= onedollar
print(str(m//quarter) + " quarters")
m %= quarter
print(str(m//dime) + " dimes")
m %= dime
print(str(m//nickel) + " nickels")
m %= nickel
print(str(m)+" pennies")