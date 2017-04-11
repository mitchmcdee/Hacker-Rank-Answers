def getPluses(i, j, n):
    if i-n < 0 or i+n >= len(g[j]) or j-n < 0 or j+n >= len(g):
        pass
        
    elif g[j][i-n] == 'G' and g[j][i+n] == 'G' and g[j-n][i] == 'G' and g[j+n][i] == 'G':
        return [[i, j, n]] + getPluses(i, j, n+1)
    
    return [[i, j, n]]


def isUniquePlus(p1, p2):
    i1,j1,n1 = p1
    i2,j2,n2 = p2
    
    h1 = [[i, j1] for i in range(i1-(n1-1), i1+n1)]
    v1 = [[i1, j] for j in range(j1-(n1-1), j1+n1)]
    h2 = [[i, j2] for i in range(i2-(n2-1), i2+n2)]
    v2 = [[i2, j] for j in range(j2-(n2-1), j2+n2)]
    
    g1 = h1 + v1
    g2 = h2 + v2
    
    return len([1 for point in g1 if point in g2]) == 0


def sizeOfPlus(plus):
    return 1 + 4*(plus[2]-1)


n,m = list(map(int, input().strip().split()))
g = []
for _ in range(n):
    g.append(list(input().strip()))

p = []
for j in range(len(g)):
    for i in range(len(g[j])):
        if g[j][i] != 'G':
            continue
        for plus in getPluses(i, j, 1):
            p.append(plus)
            
p.sort(key=lambda x: x[2], reverse=True)

maxProduct = 0
for i in range(len(p)):
    for j in range(i+1, len(p)):
        # if the two pluses can't make a bigger product, don't check them
        if sizeOfPlus(p[i]) * sizeOfPlus(p[j]) <= maxProduct:
            continue
        if(isUniquePlus(p[i], p[j])):
            maxProduct = max(maxProduct, (sizeOfPlus(p[i]) * sizeOfPlus(p[j])))
                
print(maxProduct)