s = input()
print("Before:",s)
print("After:",' '.join(map(lambda s: s[:-1]+s[-1].upper(), s.title().split())))