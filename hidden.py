"""
ID: aasang1
LANG: PYTHON3
PROG: hidden
"""

fin = open("hidden.in", "r")
lines = [i.split("\n")[0] for i in fin.readlines()]
fin.close()

N = int(lines[0].split(" ")[0])
arr = [[int(j) for j in i.split(" ")] for i in lines[1:]]

maxn = 5010
