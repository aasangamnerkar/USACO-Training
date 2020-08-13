"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: hamming
"""

INPUTFILE = "hamming.in"
OUTFILE = "hamming.out"


fin = open (INPUTFILE, 'r')

line = fin.readline()
N, B, D = line.split(" ")
N, B, D = int(N), int(B), int(D)
fin.close()


def hammingDistance(nums, num, D):
    for n in nums:
        if bin(n ^ num).count("1") < D:
            return False
    return True

nums = []
num = 0
output = []
while len(nums) < N:
    if hammingDistance(nums, num, D) or num == 0:
        nums.append(num)
    num += 1



output = ""
for i, n in enumerate(nums):
    if i > 0 and i % 10 == 9:
        output += str(n) + "\n"
    elif i < len(nums)-1:
        output += str(n) + " "
    else:
        output += str(n) + "\n"

fout = open (OUTFILE, 'w')
fout.write(output)
fout.close()