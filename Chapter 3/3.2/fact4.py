"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: fact4
"""

INFILE = "fact4.in"
OUTFILE = "fact4.out"

fin = open(INFILE, 'r')

N = int(fin.readline())

fin.close()

p = 1
for i in range(2, N+1):
    p = p * i

s = str(p)
length = len(s)
output = ""
for i in range(length):
    if s[length-1-i] != "0":
        output = str(s[length-1-i])
        break

fout = open(OUTFILE, 'w')
fout.write(output + "\n")
fout.close()