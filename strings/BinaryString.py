s = input()
f = 0
for i in s:
    if i=='0' or i=='1':
        f = 1
    else:
        f=0
if f==1:
    print("Binary String")
elif f==0:
    print("Not a Binary String")