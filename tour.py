"""
ID: aasang1
LANG: PYTHON3
PROG: tour
"""

fin = open("tour.in", 'r')
in_arr = [i.split("\n")[0] for i in fin.readlines()]
fin.close()

N, V = in_arr[0].split(" ")
N, M = int(N), int(V)

maxn = 102

city = [[0 for i in range(20)] for n in range(maxn)]
g = [[False for i in range(maxn)] for n in range(maxn)]
f = [[0 for i in range(maxn)] for n in range(maxn)]

for i in range(1, N+1):
    city[i] = in_arr[i]

def get_id(s):
    for i in range(1, N+1):
        if s == city[i]:
            return i
    return 0

x, y = None, None

st = [[0 for i in range(20)] for n in range(20)]
en = [[0 for i in range(20)] for n in range(20)]

for i in range(M):
    st, en = in_arr[N+1+i].split(" ")

    x = get_id(st)
    y = get_id(en)

    if x < y:
        g[x][y] = True
    else:
        g[y][x] = True


f[1][1] = 1
ans = 1

for i in range(1, N+1):
    for j in range(i+1, N+1):
        for k in range(1, j):
            if g[k][j]:
                if k==1 and i != 1:
                    continue
                if f[i][k] > 0 and f[i][k]+ 1 > f[i][j]:
                    f[i][j] = f[i][k]+1

        f[j][i] = f[i][j]

    if i == N:
        if f[N][N]-1 > ans:
            ans = f[N][N]-1
    elif g[i][N] and f[i][N] > ans:
        ans = f[i][N]


print(ans)