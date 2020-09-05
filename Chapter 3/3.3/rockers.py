"""
ID: aasanga1
LANG: PYTHON3
PROG: rockers
"""

fin = open("rockers.in", 'r')
in_arr = [i.split("\n")[0] for i in fin.readlines()]
fin.close()

N, T, M = in_arr[0].split()
N, T, M = int(N), int(T), int(M)

songs = [int(i) for i in in_arr[1].split()]

global best
best = 0

def solve(i, n, t, m):
    global best
    if i == N:
        best = max(best, n)
        return
    solve(i+1, n, t, m)
    if T >= t+songs[i]:
        solve(i+1, n+1, t+songs[i], m)
    elif m+1 < M and T >= songs[i]:
        solve(i+1, n+1, songs[i], m+1)

solve(0,0,0,0)

fout = open("rockers.out", 'w')
fout.write(str(best) + "\n")
fout.close()