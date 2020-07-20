"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: palsquare
"""

INPUTFILE = "palsquare.in"
OUTFILE = "palsquare.out"


fin = open (INPUTFILE, 'r')
fout = open (OUTFILE, 'w')

input_array = []
for line in fin:
    input_array.append(str(line).split("\n")[0])

def reverse(s):
    return s[::-1]

import string
digs = string.digits + string.ascii_letters


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)


N = int(input_array[0])

nums_300 = []
for i in range(1, 301):
    nums_300.append([int2base(i, N).upper(), str(int2base(i*i, N)).upper()])

palindromes = []
for item in nums_300:
    if item[1] == reverse(item[1]):
        palindromes.append(item)

output = ""
for item in palindromes:
    output += str(item[0]) + " " + item[1] + "\n"

fout.write(output)