n,k = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))

count = 0
for i in range(n):
    for j in range(i, n):
        count += (a[i] + a[j]) % k == 0 and i < j

print(count)