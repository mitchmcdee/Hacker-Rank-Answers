n = int(input().strip())
a = [list(map(int, input().strip().split())) for _ in range(n)]

sumPrimary = sum([a[i][i] for i in range(n)])
sumSecondary = sum([a[(n - 1) - i][i] for i in range(n)])
    
print(abs(sumPrimary - sumSecondary))