s = input().strip()
print(1 + sum(1 for e in s if e.isupper()))