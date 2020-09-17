widgets = input("Enter the amount of widgets: ")
res1 = int(widgets)*75
gizmos = input("Enter the amount of gizmos: ")
res2 = int(gizmos)*112
res = res1+res2
res_kilo = res/1000
print("Total weight in grams: "+str(res))
print("Total weight in kilograms: " + str("%.2f" % res_kilo))