"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: money
"""

INPUTFILE = "money.in"
OUTFILE = "money.out"

fin = open(INPUTFILE, "r")

input_arr = fin.readlines()
V, N = input_arr[0].split(" ")
V, N = int(V), int(N)

coins = []
for i in input_arr[1:]:
    for coin in i.split(" "):
        coins.append(int(coin))
fin.close()

ways = [0 for i in range(N+1)]
ways[0] = 1

for i in range(len(coins)):
    for j in range(1, len(ways)):
        if j >= coins[i]:
            ways[j] += ways[j-coins[i]]


fout = open(OUTFILE, 'w')
fout.write(str(ways[N]) + "\n")
fout.close()