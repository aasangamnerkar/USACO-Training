"""
ID: aasang1
LANG: PYTHON3
PROG: range
"""

fin = open("range.in", 'r')
in_arr = [i.split("\n")[0] for i in fin.readlines()]
fin.close()
N = int(in_arr[0])

unfiltered = in_arr[1:]

data = ["lol" for i in range(N)]

for i in range(N):
    l = [char for char in unfiltered[i]]
    arr = ["lol" for a in range(N)]
    for j in range(N):
        arr[j] = l[j]!='0'

    data[i] = arr

def loop(x, y):
    for i in range(1, N - max(x, y) + 1):
        if y + 1 > N or x + i > N:
            return 0
        for y2 in range(y, y + i):
            if not data[x + i - 1][y2]:
                return 0
        for x2 in range(x, x + i - 1):
            if not data[x2][y + i - 1]:
                return 0

        sums[i] += 1

sums = [0 for i in range(N+1)]
for x in range(N):
    for y in range(N):
        lol = loop(x, y)


fout = open("range.out", 'w')
for i in range(2, N+1):
    if sums[i] == 0:
        continue
    else:
        fout.write(str(i)+" "+str(sums[i]) + "\n")

fout.close()
