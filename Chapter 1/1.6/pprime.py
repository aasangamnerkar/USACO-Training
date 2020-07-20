"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: pprime
"""
INFILE = "pprime.in"
OUTFILE = "pprime.out"

fin = open(INFILE,'r')
fout = open (OUTFILE, 'w')

a, b = str(fin.readline()).split(" ")
a, b = int(a), int(b)

def is_Prime(num):
    if num > 1:
        i = 3
        # Iterate from 2 to n / 2
        while i < num//2:
            if (num % i) == 0:
                return False
            i += 2

        else:
            return True
    else:
        return False

if a % 2 == 0:
    a = a + 1

pal = []
i = a
output = ""
while i < b:
    s = str(i)
    if s[::-1] == s:
        if is_Prime(i):
            output += s + "\n"
    i += 2

fout.write(output)