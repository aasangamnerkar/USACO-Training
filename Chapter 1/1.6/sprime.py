"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: sprime
"""

INPUTFILE = "sprime.in"
OUTFILE = "sprime.out"


fin = open (INPUTFILE, 'r')
fout = open (OUTFILE, 'w')

N = int(fin.readline())

def is_Prime(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)):
            if (num % i) == 0:
                return False

        else:
            return True
    else:
        return False

bases = [2,3,5,7]
nums = [1,3,5,7,9]

def get_pals(base, index, output):
    #print(output)
    temp_arr = []
    if index == 0:
        for num in nums:
            combined = str(base) + str(num)
            if is_Prime(int(combined)):
                temp_arr.append(combined)
        return get_pals(base, index+1, temp_arr)
    elif index < N-2:
        for item in output:
            for num in nums:
                combined = str(item) + str(num)
                if is_Prime(int(combined)):
                    temp_arr.append(combined)
        return get_pals(base, index + 1, temp_arr)
    else:
        for item in output:
            for num in [1,3,7,9]:
                combined = str(item) + str(num)
                if is_Prime(int(combined)):
                    temp_arr.append(combined)
        return temp_arr

output = ""
if N != 1:
    for base in bases:
        arr = get_pals(base, 0, [])
        for item in arr:
            output += str(item) + "\n"
else:
    for i in [1,3,5,7]:
        output += str(i) + "\n"
fout.write(output)