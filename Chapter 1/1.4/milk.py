"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: milk
"""

INPUTFILE = "milk.in"
OUTFILE = "milk.out"


fin = open (INPUTFILE, 'r')
fout = open (OUTFILE, 'w')

input_array = []
for line in fin:
    input_array.append(str(line).split("\n")[0])

N, M = int(input_array[0].split(" ")[0]), int(input_array[0].split(" ")[1])
prices = []
for i in range(1, len(input_array)):
    price, units = int(input_array[i].split(" ")[0]), int(input_array[i].split(" ")[1])
    prices.append([price, units])

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

#prices = insertionSort(prices)
#quickSort(prices, 0, len(prices)-1)
mergeSort(prices, 0, len(prices)-1)
done = False
bought = 0
price = 0
i = 0
while not done:
    if bought < N:
        current_farmer = prices[i]
        if bought + current_farmer[1] < N:
            bought = bought + current_farmer[1]
            price = price + (current_farmer[1]*current_farmer[0])
        else:
            units_bought = N - bought
            bought = N
            price = price + (units_bought*current_farmer[0])
        i += 1
    else:
        done = True

fout.write(str(price) + "\n")
