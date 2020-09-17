print("""Enter number of the bottles holding one liter 
or less which you want to recycle: """, end = "")
less_than_one = int(input())
money = less_than_one *(0.10)
print("""Enter number of the bottles that more than 
one liter which you want to recycle: """, end = "")
more_than_one = int(input())
money2 = more_than_one*(0.25)
res = money+money2
if(res*10 == int(res*10)):
    print("Your deposit: "+str(res)+"0 $")
else:
    print("Your deposit: "+str(res)+" $")