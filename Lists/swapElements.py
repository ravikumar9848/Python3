n = int(input())
print("Enter the Elements:")
l = list()
for i in range(n):
    l.append(int(input()))
if len(l)>=2:
    print("Before Swaping:",l)
    l[0],l[n-1] = l[n-1],l[0]
    print("After Swapping :",l)
else:
    print("List has less than 2 elements")