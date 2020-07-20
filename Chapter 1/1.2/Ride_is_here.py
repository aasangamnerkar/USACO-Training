"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: ride
"""

INPUTFILE = "ride.in"
OUTFILE = "ride.out"


fin = open (INPUTFILE, 'r')
fout = open (OUTFILE, 'w')

input_array = []

for line in fin:
    input_array.append(str(line).split("\n")[0])

def calculate_product(s):
    string_array = [char for char in s.upper()]
    number_array = []

    for char in string_array:
        number_array.append(ord(char)-64)

    product = 1
    for number in number_array:
        product = product*number

    return product % 47

number_array = []
for input in input_array:
    number_array.append(calculate_product(input))

if (number_array[0] == number_array[1]):
    fout.write("GO\n")
else:
    fout.write("STAY\n")