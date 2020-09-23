"""
ID: aasang1
LANG: PYTHON3
PROG: stall4
"""

fin = open("stall4.in", 'r')
in_arr = [i.split("\n")[0] for i in fin.readlines()]
fin.close()

N, M = in_arr[0].split(" ")
N, M = int(N), int(M)

arr = [[int(i) for i in j.split(" ")] for j in in_arr[1:]]

mapn = [[None for i in range(402)] for j in range(402)]

Next = [0 for i in range(400)]
mark = [False for i in range(400)]

tot = 0

def check(x):
    for i in range(0, M+1):
        if mapn[x][i] and (not mark[i]):
            mark[i] = True
            if Next[i]==0 or check(Next[i]):
                Next[i] = x
                return True

    return False

for i in range(1, N):
    for b in arr[i][1:]:
        mapn[i][b] = True

for i in range(1, N+1):
    for j in range(1, M+1):
        mark[j] = False

    if check(i):
        tot += 1


fout = open("stall4.out", 'w')
fout.write(str(tot) + "\n")
fout.close()