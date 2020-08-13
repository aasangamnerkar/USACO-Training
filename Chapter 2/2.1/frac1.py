"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: frac1
"""

INPUTFILE = "frac1.in"
OUTFILE = "frac1.out"


fin = open (INPUTFILE, 'r')
fout = open (OUTFILE, 'w')



def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i][0] <= R[j][0]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

MAX_DENOM = int(fin.readline())
fin.close()

arr = [[0, "0/1"]]
f = []
for N in range(1, MAX_DENOM+1):
    for i in range(1, N):
        div = float(i/N)
        if div not in f:
            arr.append([div, str(i)+"/"+str(N)])
            f.append(div)

mergeSort(arr, 0, len(arr)-1)

output = ""
for item in arr:
    output += item[1] + "\n"
output += "1/1\n"

fout.write(output)

fout.close()