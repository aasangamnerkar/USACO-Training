"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: gift1
"""

INPUTFILE = "gift1.in"
OUTFILE = "gift1.out"


fin = open (INPUTFILE, 'r')

input_array = []
for line in fin:
    count_array = []
    input_array.append(str(line).split("\n")[0])

fout = open (OUTFILE, 'w')

giver_array = []
money_array = []
reciever_array = []
split_array = []
index_array = []
total_array = []

np = int(input_array[0])

def contains_digit(s):
    contains_digit = False
    for char in s:
        if char.isdigit():
            return True
    return False

def get_index(s):
    for i in range(0, len(total_array)):
        if total_array[i][0] == s:
            return i
    return -1

ready = False
giver_indexes = []
i = 1
while i < len(input_array):
    if not ready:
        has_digit = contains_digit(input_array[i + 1])

        if has_digit:
            ready = True

    if ready:
        if contains_digit(input_array[i]):
            money_array.append(int(input_array[i].split(" ")[0]))
            split_array.append(int(input_array[i].split(" ")[1]))
            if (i < len(input_array)):
                giver_array.append(input_array[i-1])
                giver_indexes.append(i-1)
                i += 1
    else:
        giver_indexes.append(i)
        total_array.append([input_array[i], 0])
    i+=1

for i in range(np, len(input_array)):
    isNotGiver = True
    for a in giver_indexes:
        if i == a:
            isNotGiver = False
    if ((contains_digit(input_array[i]) == False) and isNotGiver):
        reciever_array.append(input_array[i])


sum = 0
index_array = [0]
for integer in split_array:
    sum += integer
    index_array.append(sum)
index_array[0] = 0

for i in range(0, len(giver_array)):
    total_array[get_index(giver_array[i])][1] -= money_array[i]  # add total to giver
    if split_array[i] != 0:
        remainder = money_array[i] % split_array[i]
        amount_dist = money_array[i]//split_array[i]
    else:
        remainder = 0
        amount_dist = money_array[i]

    for index in range(index_array[i], index_array[i+1]):
        total_array[get_index(reciever_array[index])][1] += amount_dist

    total_array[get_index(giver_array[i])][1] += remainder #add total to giver

output = ""
for item in total_array:
    output += item[0] + " " + str(item[1]) + "\n"

fout.write(output)