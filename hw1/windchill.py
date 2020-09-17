ta = float(input("Enter the air temperature: "))
v = float(input("Enter the wind speed: "))
par = 13.12
par_2 = 0.6215
par_3 = 11.37
par_4 = 0.3965
p = 0.16
if (ta<=10 and v>4.8):
    res = par+(par_2*ta)-(par_3*(v**p))+(par_4*ta*(v**p))
    print("The Wind Chill Index equals to %.2f" %res)
else:
    print("Wrong data!")