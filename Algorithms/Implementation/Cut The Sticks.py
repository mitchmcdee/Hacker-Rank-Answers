n = int(input().strip())
arr = sorted(list(map(int, input().strip().split())))

while len(arr) > 0:
    print(len(arr))
    arr = [e - arr[0] for e in arr]
    
    while len(arr) != 0 and arr[0] <= 0:
        arr.pop(0)