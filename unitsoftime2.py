s = int(input("Enter the seconds that have been passed: "))
days = s//86400
s %= 86400
hours = s//3600
s %= 3600
minutes= s//60
s %= 60
seconds = s
print("Time duration: "+str(days)+":", end = "")
print("%02.d:%.02d:%.02d" %(hours, minutes, seconds))