
  
from itertools import permutations

s = input()
permList = permutations(s)
for perm in list(permList):
    print (''.join(perm))