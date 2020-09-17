a = [int(i) for i in input().split()]
maxi = max(a)
mini =min(a)
mid = sum(a)-maxi-mini
print("Maximum:", maxi)
print("Minimum:", mini)
print("The middle value:", mid)