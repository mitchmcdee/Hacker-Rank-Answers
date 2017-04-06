n,k,q = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))

rotated = []
for i in range(n):
    pos = i - (k % n)
    if pos >= 0:
        rotated.append(a[pos])
    else:
        rotated.append(a[pos + n])
        
for query in range(q):
    m = int(input().strip())
    print(rotated[m])