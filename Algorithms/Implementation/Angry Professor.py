t = int(input().strip())
for _ in range(t):
    n,k = list(map(int, input().strip().split()))
    a = sorted(list(map(int, input().strip().split())))
    
    print("YES" if a[k-1] > 0 else "NO")