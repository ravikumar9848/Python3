l = list(map(int,input().split()))
print(max(l))
max = 0
for i in l:
    if i>max:
        max = i
print(max)


