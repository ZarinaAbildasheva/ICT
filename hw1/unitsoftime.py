print("Enter the number of days, hours, minutes, seconds by space: ", end = "")
days, hours, minutes, seconds = [int(i) for i in input().split()]
res = (minutes*60) + seconds + (hours*3600) + (days*3600*24)
print(res, "seconds passed")