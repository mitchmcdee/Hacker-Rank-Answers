d1,d2,k = list(map(int, input().strip().split()))

beautiful = 0
for d in range(d1, d2+1):
    r = int(str(d)[::-1])
    beautiful += (d-r)%k == 0
    
print(beautiful)