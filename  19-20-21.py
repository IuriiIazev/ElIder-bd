a = [[0] * 147 for t in range(147)]

for i in range(76,7,-1):
    for j in range(76,1,-1):
        if i + j >= 77:
            a[i][j] = 0
        elif ((a[i+1][j] == 0) or (a[i*2][j] == 0) or (a[i][j+1] == 0) or (a[i][j*2] == 0)):
            print(a)
            a[i][j] = 1
        elif ((i + j < 77) and (a[i+1][j] > 0 and a[i*2][j] > 0 and a[i][j+1] > 0 and a[i][j*2] > 0)):
            a[i][j] = -max([a[i+1][j],a[i*2][j],a[i][j+1],a[i][j*2]]) - 1
        else:
            temp = [a[i+1][j],a[i*2][j],a[i][j+1],a[i][j*2]]
            g = [i for i in temp if i < 0]
            a[i][j] = -max(g) + 1

for r in range(len(a)):
    for t in range(len(a[r])):
        if a[r][t] == 3:
            print(r,t)