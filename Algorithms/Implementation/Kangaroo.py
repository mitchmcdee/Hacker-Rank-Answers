x1,v1,x2,v2 = list(map(int, input().strip().split()))

if x2 > x1 and v2 > v1 or v1 == v2:
    print("NO")
else:
    print("YES" if (x1 - x2) % (v2 - v1) == 0 else "NO")