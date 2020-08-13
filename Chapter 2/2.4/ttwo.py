"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: ttwo
"""

INPUTFILE = "ttwo.in"
OUTFILE = "ttwo.out"

fin = open(INPUTFILE, 'r')

input_array = [line.split("\n")[0] for line in fin.readlines()]

fin.close()

grid = [[char for char in col] for col in input_array]

dirX = [1, 0, -1, 0]
dirY = [0, 1, 0, -1]

farmerX = -1
farmerY = -1
farmerDir = 3

cowXs = []
cowYs = []
cowDirs = []

for i in range(10):
    for j in range(10):
        if grid[i][j] == "F":
            print("FOUND IT")
            farmerX = j
            farmerY = i
            grid[i][j] = "."
        elif grid[i][j] == "C":
            print("FOUND COW")
            cowXs.append(j)
            cowYs.append(i)
            cowDirs.append(3)
            grid[i][j] = "."


works = False
mins = 0

while not works:
    x = farmerX + dirX[farmerDir]
    y = farmerY + dirY[farmerDir]

    if x >= 10 or x < 0 or y >= 10 or y < 0 or grid[y][x] == "*":
        farmerDir += 1
        farmerDir %= 4
    else:
        farmerX = x
        farmerY = y

    for i in range(len(cowXs)):
        x = cowXs[i] + dirX[cowDirs[i]]
        y = cowYs[i] + dirY[cowDirs[i]]

        if x >= 10 or x < 0 or y >= 10 or y < 0 or grid[y][x] == "*" or grid[y][x] == "C":
            cowDirs[i] = (cowDirs[i]+1)%4
        else:
            cowXs[i] = x
            cowYs[i] = y

        if cowXs[i] == farmerX and cowYs[i] == farmerY:
            works = True

    if mins > 100000:
        break

    mins += 1

fout = open(OUTFILE, 'w')

if works:
    fout.write(str(mins) + "\n")
else:
    fout.write(str(0) + "\n")

fout.close()