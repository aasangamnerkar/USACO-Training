"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: transform
"""

INPUTFILE = "transform.in"
OUTFILE = "transform.out"


fin = open (INPUTFILE, 'r')
fout = open (OUTFILE, 'w')


input_array = []
for line in fin:
    count_array = []
    input_array.append(str(line).split("\n")[0])

N = int(input_array[0])
input_square = ([list(input_array[item]) for item in range(1, N+1)])
out_square = ([list(input_array[item]) for item in range(N+1, (2*N)+1)])

def rot90(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]) - 1, -1, -1)]

def rot(arr, n):
    rotate = arr.copy()
    for i in range(0, n):
        rotate = rot90(rotate)
    return rotate

def check_90(in_array, rotate_array):
    if (rot(in_array, 3) == rotate_array):
        return True
    return False

def check_180(in_array, rotate_array):
    if (rot(in_array, 2) == rotate_array):
        return True
    return False

def check_270(in_array, rotate_array):
    if (rot(in_array, 1) == rotate_array):
        return True
    return False

def check_reflect(m, arr2):
    reflect = []
    for row in m:
        temp_array = []
        for column in row:
            temp_array.append(column)
        reflect.append(temp_array)
    arr1 = m
    for row in range(0, N):
        for column in range(0, N):
            reflect[row][N-1-column] = arr1[row][column]

    if (reflect == arr2):
        return True
    return False

def check_combo(m, arr2):
    reflect = []
    for row in m:
        temp_array = []
        for column in row:
            temp_array.append(column)
        reflect.append(temp_array)
    arr1 = m
    for row in range(0, N):
        for column in range(0, N):
            reflect[row][N-1-column] = arr1[row][column]

    if(check_90(reflect, arr2)):
        return 90
    elif(check_180(reflect, arr2)):
        return 180
    elif(check_270(reflect, arr2)):
        return 270
    return -1

def check_none(arr1, arr2):
    if(arr1==arr2):
        return True
    return False


output = 7

if check_90(input_square, out_square):
    output = 1
elif check_180(input_square, out_square):
    output = 2
elif check_270(input_square, out_square):
    output = 3
elif check_reflect(input_square, out_square):
    output = 4
elif check_combo(input_square, out_square) != -1:
    output = 5
elif check_none(input_square, out_square):
    output = 6

fout.write(str(output) + "\n")
