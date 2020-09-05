"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: inflate
"""

INFILE = "inflate.in"
OUTFILE = "inflate.out"

fin = open(INFILE, 'r')
input_arr = [line.split('\n')[0] for line in fin.readlines()]
fin.close()

line = input_arr[0].split()
arr = []
for i in line:
    if i.isdigit():
        arr.append(i)
M,N = int(arr[0]), int(arr[1])

questions = [[int(j) for j in i.split(" ")] for i in input_arr[1:]]

if N < 10:
    min = questions[0][0]
    for i in questions:
        if i[0] < min:
            min = i[0]

    data = [min for i in range(M+1)]
else:
    data = [0 for i in range(M+1)]

for i in range(N):
    points = questions[i][0]
    minutes = questions[i][1]
    for j in range(minutes, M):
        if data[j] < data[j-minutes] + points:
            data[j] = data[j-minutes] + points

fout = open(OUTFILE, "w")
fout.write(str(data[M-1]) + "\n")
fout.close()