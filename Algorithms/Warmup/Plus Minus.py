n = int(input().strip())
arr = list(map(int, input().strip().split()))

positive = 0
negative = 0
zero = 0
for element in arr:
    if element > 0:
        positive += 1
    elif element < 0:
        negative += 1
    else:
        zero += 1

length = len(arr)
print(float(positive) / length)
print(float(negative) / length)
print(float(zero) / length)