"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: namenum
"""

INPUTFILE = "namenum.in"
OUTFILE = "namenum.out"


fin = open (INPUTFILE, 'r')
fout = open (OUTFILE, 'w')

fdict = open("dict.txt", 'r')

input_array = []
for line in fin:
    input_array.append(str(line).split("\n")[0])

unsorted_names = []
for line in fdict:
    unsorted_names.append(str(line).split("\n")[0])

def get_letters(num):
    if num == 0:
        return [""]
    elif num == 2:
        return ['A', 'B', 'C']
    elif num == 3:
        return ['D', 'E', 'F']
    elif num == 4:
        return ['G', 'H', 'I']
    elif num == 5:
        return ['J', 'K', 'L']
    elif num == 6:
        return ['M', 'N', 'O']
    elif num == 7:
        return ['P', 'R', 'S']
    elif num == 8:
        return ['T', 'U', 'V']
    elif num == 9:
        return ['W', 'X', 'Y']


def search_name(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return search_name(arr, low, mid - 1, x)
        else:
            return search_name(arr, mid + 1, high, x)

    else:
        return -1

def get_split(arr, index):
    output = []
    if index < len(serial_num):
        char_array = get_letters(serial_num[index])
        c1 = char_array[0]
        c2 = char_array[1]
        c3 = char_array[2]
        for name in arr:
            if len(name) == len(serial_num):
                if name[index] == c1 or name[index] == c2 or name[index] == c3:
                    output.append(name)
        return get_split(output, index+1)
    else:
        out = []
        for item in arr:
            out.append(item)
        return out


serial_num = [int(char) for char in input_array[0]]
split = get_letters(serial_num[0])

letter_array = [get_letters(number) for number in serial_num]
possible_names = get_split(unsorted_names, 0)



search_query = ""

if len(possible_names) > 0:
    output = ""
    for i in range(len(possible_names)):
        output += possible_names[i] + "\n"
else:
    output = "NONE\n"
fout.write(output)
