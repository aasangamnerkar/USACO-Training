"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: dualpal
"""

INPUTFILE = "dualpal.in"
OUTFILE = "dualpal.out"


fin = open (INPUTFILE, 'r')
fout = open (OUTFILE, 'w')

input_array = []
for line in fin:
    input_array.append(str(line).split("\n")[0])

N, S = int(input_array[0].split(" ")[0]), int(input_array[0].split(" ")[1])

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

    return ''.join(digits).upper()

def check_palindromic(num):
    counter = 0
    for i in range(2, 11):
        converted = int2base(num, i)
        if reverse(converted) == converted:
            counter += 1
    if counter > 1:
        return True
    return False

nums_10k = []
for i in range(S+1, 100000):
    nums_10k.append(i)

palindromes = []
done = False
i = 0
while not done:
    if i < len(nums_10k) and len(palindromes) < N:
        item = nums_10k[i]
        isPal = check_palindromic(nums_10k[i])
        if isPal:
            palindromes.append(nums_10k[i])
    else:
        done = True
    i += 1

output = ""
for item in palindromes:
    output += str(item)+ "\n"

fout.write(output)