seen = 5
like = 0
for _ in range(int(input())):
    like += seen // 2
    seen = (seen // 2) * 3
print(like)