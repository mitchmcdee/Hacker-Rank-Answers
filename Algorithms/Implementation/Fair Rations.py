n = int(input().strip())
b = list(map(int, input().strip().split()))

count = 0
for i in range(n-1):
    if b[i]%2:
        #never look at b[i] again, don't need to increment it
        b[i+1] +=1
        count += 2
        
print('NO' if b[n-1]%2 else count)