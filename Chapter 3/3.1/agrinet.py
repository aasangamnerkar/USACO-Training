"""
ID: aasangamnerkar
LANG: PYTHON3
PROG: agrinet
"""

IN_FILE = "agrinet.in"
OUT_FILE = "agrinet.out"

fin = open(IN_FILE, 'r')

input_arr = fin.readlines()
N = int(input_arr[0])

unfiltered_arr = []
for line in input_arr[1:]:
    i = line.split("\n")[0]
    for j in i.split(" "):
        unfiltered_arr.append(int(j))

fin.close()

arr = []
i = 0
temp_arr = []

iter_arr = iter(unfiltered_arr)
for i in range(N):
    temp_arr = []
    for j in range(N):
        temp_arr.append(next(iter_arr))
    arr.append(temp_arr)
while i < len(unfiltered_arr):
    if len(temp_arr) == 35:
        arr.append(temp_arr)
        temp_arr = []
    else:
        temp_arr.append(unfiltered_arr[i])
    i += 1


class Node:
    def __init__(self, dist, inTree, source):
        self.distance = dist
        self.inTree = inTree
        self.source = source

    def __init__(self):
        self.distance = "NO"
        self.inTree = False
        self.source = -1

    def set(self):
        self.distance = "NO"
        self.inTree = False
        self.source = -1

nodes = [Node() for i in range(N)]

treesize = 1
treecost = 0

#initializing the nodes array
nodes[0].inTree = True
nodes[0].distance = 0
nodes[0].source = -1

for j in range(1, N):
    if arr[0][j] != -1:
        nodes[j].distance = arr[0][j]
        nodes[j].source = 0

done = False
while treesize < N and (not done):
    mini = 0
    min = 100000
    for i in range(N):
        if (not nodes[i].inTree) and nodes[i].distance < min:
            min = nodes[i].distance
            mini = i

    if min == "NO":
        done = True

    treesize += 1
    treecost += min
    nodes[mini].inTree = True

    for j in range(N):
        if nodes[j].distance > arr[mini][j]:
            nodes[j].distance = arr[mini][j]
            nodes[j].source = mini


res = treecost

fout = open(OUT_FILE, 'w')
fout.write(str(res) + "\n")
fout.close()