n = int(input().strip())
sides = sorted(list(map(int, input().strip().split())))

i = n-3
while i >= 0 and (sides[i] + sides[i+1] <= sides[i+2]):
    i -= 1

print(" ".join(str(e) for e in sides[i:i+3]) if i >= 0 else "-1")