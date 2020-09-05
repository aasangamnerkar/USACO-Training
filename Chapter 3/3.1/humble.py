"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: humble
"""

INFILE = "humble.in"
OUTFILE = "humble.out"

fin = open(INFILE, 'r')
K, N = fin.readline().split()
K, N = int(K), int(N)

nums = [int(i) for i in fin.readline().split()]


humbles = [0 for i in range(N+1)]
next = [0 for i in range(K)]
humbles[0] = 1

max = 10**5000

for i in range(1, N+1):
    best = max
    for j in range(K):
        while next[j] < i and (humbles[next[j]]*nums[j]) <= humbles[i-1]:
            next[j] += 1
        best = min(best, (nums[j]*humbles[next[j]]))
    humbles[i] = best

fout = open(OUTFILE, 'w')
fout.write(str(humbles[N]) + "\n")
fout.close()