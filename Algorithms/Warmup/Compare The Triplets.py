a0, a1, a2 = list(map(int, input().strip().split()))
b0, b1, b2 = list(map(int, input().strip().split()))

aPoints = int(a0 > b0) + int(a1 > b1) + int(a2 > b2)
bPoints = int(b0 > a0) + int(b1 > a1) + int(b2 > a2)

print("{0} {1}".format(aPoints, bPoints))