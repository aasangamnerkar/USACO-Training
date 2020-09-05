"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: stamps
"""

INFILE = "stamps.in"
OUTFILE = "stamps.out"

fin = open(INFILE, 'r')

input_arr = [i.split("\n")[0] for i in fin.readlines()]
fin.close()

K, N = input_arr[0].split()
K, N = int(K), int(N)

arr = [[int(k) for k in i.split()] for i in input_arr[1:]]

coins = []
for i in arr:
    for j in i:
        coins.append(j)

m = 10000**10
coins.sort()
minimums = [m for i in range(K*coins[N-1]+1)]
minimums[0] = 0

finished = False
while not finished:
    finished = True
    for i in range(N):
        j = 0
        while j+coins[i] < len(minimums):
            newer = minimums[j]+1
            old = minimums[j+coins[i]]
            if newer < old:
                finished = False
                minimums[j+coins[i]] = newer
            j += 1

i = 0
while i < len(minimums):
    if minimums[i] > K:
        break
    i += 1

fout = open(OUTFILE, 'w')
fout.write(str(i-1)+"\n")
fout.close()