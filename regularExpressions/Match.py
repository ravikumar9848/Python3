
import re

string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string) 

if match:
  print(match.group())
else:
  print("pattern not found")

# Output: 801 35
print(match.group(1))
print(match.group(2))
print(match.group(1,2))
print(match.start())
print(match.end())
print(match.re)
print(match.string)