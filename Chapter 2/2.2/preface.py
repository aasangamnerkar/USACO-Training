"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: preface
"""

INPUTFILE = "preface.in"
OUTFILE = "preface.out"


fin = open(INPUTFILE, 'r')

N = int(fin.readline())

fin.close()

totals = [0, 0, 0, 0, 0, 0, 0]
values = [1, 5, 10, 50, 100, 500, 1000]
symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

for num in range(N+1):
    n = num

    i = len(totals)-1
    while i >= 0:
        times = n // values[i]
        if times == 9:
            totals[i] += 1
            totals[i + 2] += 1
        elif times > 4:
            totals[i+1] += 1
            totals[i] += times - 5
        elif times == 4:
            totals[i] += 1
            totals[i+1] += 1
        else:
            totals[i] += times

        n -= values[i] * times

        i -= 2
output = ""
for i, item in enumerate(totals):
    if item != 0:
        output += str(symbols[i]) + " " + str(item) + "\n"
print(output)
fout = open(OUTFILE, 'w')
fout.write(output)
fout.close()