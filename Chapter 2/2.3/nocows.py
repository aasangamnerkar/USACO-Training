"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: nocows
"""

INPUTFILE = "nocows.in"
OUTFILE = "nocows.out"

fin = open(INPUTFILE, "r")
N, K = fin.readline().split(" ")
N, K = int(N), int(K)

results = [[-1 for i in range(K+1)] for i in range(N+1)]

def solve(N, K):
    if results[N][K] != -1:
        return results[N][K]
    elif (N < 1 or K < 1 or 2*K-1>N or N%2==0):
        return 0
    elif N == 1:
        if K == 1:
            return 1

        return 0

    results[N][K] = 0

    for i in range(1, N-1):
        temp = N - i - 1
        for j in range(K-1):
            results[N][K] += solve(i, j) * solve(temp, K-1)
            results[N][K] += solve(i, K-1) * solve(temp, j)

        results[N][K] += solve(i, K-1) * solve(temp, K-1)

    results[N][K] %= 9901
    return results[N][K]

fout = open(OUTFILE, "w")
fout.write(str(solve(N, K)) + "\n")