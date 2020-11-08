"""
ID: aasang1
LANG: PYTHON3
PROG: bigbrn
"""

fin = open("bigbrn.in", 'r')
in_arr = [i.split("\n")[0] for i in fin.readlines()]
fin.close()

N, T = in_arr[0].split(" ")
N, T = int(N), int(T)


def maximalSquare(matrix):
    rows = len(matrix)
    if rows > 0:
        cols = len(matrix[0])
    else:
        cols = 0
    dp = [[0 for n in range(cols+1)] for i in range(rows+1)]
    maxsqlen = 0
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            if matrix[i-1][j-1] == ".":
                dp[i][j] = min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1
                maxsqlen = max(maxsqlen, dp[i][j])

    return maxsqlen

grid = [['.' for n in range(N)] for i in range(N)]

for i in range(T):
    x, y = in_arr[i+1].split(" ")
    x, y = int(x) - 1, int(y) - 1

    grid[x][y] = "#"

output = maximalSquare(grid)

fout = open("bigbrn.out", 'w')
fout.write(str(output) + "\n")
fout.close()