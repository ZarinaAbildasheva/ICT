s1, s2, s3 = [int(i) for i in input("Enter the length of all 3 sides: ").split()]
p = (s1+s2+s3)/2
area = p*(p-s1)*(p-s2)*(p-s3)
res = area**(1/2)
print("Calculated area equals to ", res)